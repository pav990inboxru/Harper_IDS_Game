import tkinter as tk
from tkinter import ttk, filedialog, messagebox, PhotoImage
import json
import os
from PIL import Image, ImageTk

class StayOutMarketTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Таблицы рынка Stay Out - Harper_IDS")
        self.root.geometry("1000x700")
        
        # Стилизация интерфейса в стиле СТАЛКЕР
        self.setup_stalker_theme()
        
        # Данные для таблиц
        self.categories = {}
        self.current_category = None
        self.current_item = None
        
        # Загрузка данных
        self.load_data()
        
        # Создание интерфейса
        self.create_widgets()
        
        # Привязка обработчика закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_stalker_theme(self):
        """Настройка темы в стиле СТАЛКЕР"""
        style = ttk.Style()
        style.theme_use("clam")
        
        # Цвета в стиле СТАЛКЕР
        self.colors = {
            'bg': '#2a2a2a',      # Темно-серый фон
            'fg': '#c0c0c0',      # Светло-серый текст
            'accent': '#4a752c',   # Зеленый акцент (как у артефактов)
            'header': '#5a5a5a',   # Заголовки
            'button': '#4a5a3a',   # Кнопки в стиле сталкера
            'button_hover': '#5a6a4a',
            'entry_bg': '#1a1a1a',
            'entry_fg': '#d0d0d0'
        }
        
        # Настройка стилей
        style.configure("TFrame", background=self.colors['bg'])
        style.configure("TLabel", background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure("TButton", background=self.colors['button'], 
                       foreground=self.colors['fg'])
        style.configure("TEntry", fieldbackground=self.colors['entry_bg'], 
                       foreground=self.colors['entry_fg'])
        style.configure("TCombobox", fieldbackground=self.colors['entry_bg'], 
                       foreground=self.colors['entry_fg'])
        style.configure("Treeview", background=self.colors['entry_bg'], 
                       foreground=self.colors['fg'], fieldbackground=self.colors['entry_bg'])
        style.configure("Treeview.Heading", background=self.colors['header'], 
                       foreground=self.colors['fg'])
        
        # Установка фона окна
        self.root.configure(bg=self.colors['bg'])
        
    def create_widgets(self):
        """Создание виджетов интерфейса"""
        # Главная вкладка
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Вкладка создания таблиц
        self.create_main_tab()
        
        # Вкладка библиотеки
        self.create_library_tab()
        
        # Вкладка ссылок
        self.create_links_tab()
        
    def create_main_tab(self):
        """Создание основной вкладки"""
        main_frame = ttk.Frame(self.notebook)
        self.notebook.add(main_frame, text="Создание таблиц")
        
        # Левая панель - категории
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_frame, text="Категории:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        # Список категорий
        self.category_listbox = tk.Listbox(left_frame, height=15, bg=self.colors['entry_bg'], 
                                          fg=self.colors['fg'], selectbackground=self.colors['accent'])
        self.category_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        self.category_listbox.bind('<<ListboxSelect>>', self.on_category_select)
        
        # Кнопки управления категориями
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Добавить", command=self.add_category).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Удалить", command=self.delete_category).pack(side=tk.LEFT, padx=2)
        
        # Правая панель - детали категории
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Заголовок категории
        self.category_title = ttk.Label(right_frame, text="Выберите категорию", 
                                       font=("Arial", 14, "bold"))
        self.category_title.pack(anchor=tk.W, pady=5)
        
        # Таблица товаров
        columns = ("Название", "Мин. цена покупки", "Цена продажи", "Кладовщик", "Место продажи", "Иконка")
        self.items_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.items_tree.heading(col, text=col)
            self.items_tree.column(col, width=120)
        
        self.items_tree.pack(fill=tk.BOTH, expand=True, pady=5)
        self.items_tree.bind('<<TreeviewSelect>>', self.on_item_select)
        
        # Фрейм для добавления/редактирования товаров
        item_frame = ttk.Frame(right_frame)
        item_frame.pack(fill=tk.X, pady=5)
        
        # Поля ввода
        ttk.Label(item_frame, text="Название товара:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.item_name = ttk.Entry(item_frame, width=20)
        self.item_name.grid(row=0, column=1, padx=5)
        
        ttk.Label(item_frame, text="Мин. цена покупки:").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.buy_price = ttk.Entry(item_frame, width=10)
        self.buy_price.grid(row=0, column=3, padx=5)
        
        ttk.Label(item_frame, text="Цена продажи:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.sell_price = ttk.Entry(item_frame, width=10)
        self.sell_price.grid(row=1, column=1, padx=5)
        
        ttk.Label(item_frame, text="Кладовщик:").grid(row=1, column=2, sticky=tk.W, padx=5)
        self.vendor = ttk.Entry(item_frame, width=20)
        self.vendor.grid(row=1, column=3, padx=5)
        
        ttk.Label(item_frame, text="Место продажи:").grid(row=2, column=0, sticky=tk.W, padx=5)
        self.location = ttk.Entry(item_frame, width=20)
        self.location.grid(row=2, column=1, padx=5)
        
        # Кнопки управления товарами
        btn_frame2 = ttk.Frame(item_frame)
        btn_frame2.grid(row=3, column=0, columnspan=4, pady=10)
        
        ttk.Button(btn_frame2, text="Добавить/Обновить", command=self.add_update_item).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame2, text="Удалить", command=self.delete_item).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame2, text="Добавить иконку", command=self.add_icon).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame2, text="Добавить ссылку", command=self.add_link).pack(side=tk.LEFT, padx=5)
        
        # Поле для иконки
        self.icon_label = ttk.Label(right_frame, text="Иконка не выбрана")
        self.icon_label.pack(pady=5)
        
        # Поле для ссылки
        link_frame = ttk.Frame(right_frame)
        link_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(link_frame, text="Ссылка на товар:").pack(anchor=tk.W)
        self.item_link = ttk.Entry(link_frame, width=60)
        self.item_link.pack(fill=tk.X, pady=2)
        
    def create_library_tab(self):
        """Создание вкладки библиотеки"""
        library_frame = ttk.Frame(self.notebook)
        self.notebook.add(library_frame, text="Библиотека таблиц")
        
        ttk.Label(library_frame, text="Сохраненные таблицы", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Список сохраненных таблиц
        self.saved_tables_listbox = tk.Listbox(library_frame, height=20, bg=self.colors['entry_bg'], 
                                              fg=self.colors['fg'], selectbackground=self.colors['accent'])
        self.saved_tables_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Кнопки управления
        btn_frame = ttk.Frame(library_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Загрузить", command=self.load_selected_table).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Удалить", command=self.delete_saved_table).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Экспорт", command=self.export_table).pack(side=tk.LEFT, padx=5)
        
    def create_links_tab(self):
        """Создание вкладки ссылок"""
        links_frame = ttk.Frame(self.notebook)
        self.notebook.add(links_frame, text="Полезные ссылки")
        
        ttk.Label(links_frame, text="Официальные ресурсы игры", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Ссылки на ресурсы
        links_data = [
            ("Википедия игры", "https://so-wiki.ru/"),
            ("Игра в Steam", "https://store.steampowered.com/app/1180380/Stay_Out/"),
            ("Профиль разработчика", "https://steamcommunity.com/id/Harper_IDS/"),
            ("Сообщество IgromanDS", "https://игроманы.рф")  # Условная ссылка
        ]
        
        for text, url in links_data:
            frame = ttk.Frame(links_frame)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            ttk.Label(frame, text=text + ":", font=("Arial", 10, "bold")).pack(anchor=tk.W)
            link_label = tk.Label(frame, text=url, fg="#4a752c", cursor="hand2", bg=self.colors['bg'])
            link_label.pack(anchor=tk.W)
            link_label.bind("<Button-1>", lambda e, u=url: self.open_url(u))
        
        # Информация об авторе
        ttk.Label(links_frame, text="\nАвтор: Harper_IDS", font=("Arial", 12, "bold")).pack(pady=10)
        ttk.Label(links_frame, text="Создано для игрового сообщества IgromanDS", font=("Arial", 10)).pack()
        
        ttk.Label(links_frame, text="Программа создана для упрощения отслеживания цен на доске объявлений в игре Stay Out", 
                 wraplength=400).pack(pady=20)
        
    def add_category(self):
        """Добавление новой категории"""
        name = tk.simpledialog.askstring("Новая категория", "Введите название категории:")
        if name:
            if name not in self.categories:
                self.categories[name] = []
                self.category_listbox.insert(tk.END, name)
                self.save_data()
            else:
                messagebox.showwarning("Предупреждение", "Категория с таким именем уже существует!")
    
    def delete_category(self):
        """Удаление категории"""
        selection = self.category_listbox.curselection()
        if selection:
            index = selection[0]
            name = self.category_listbox.get(index)
            if messagebox.askyesno("Подтверждение", f"Удалить категорию '{name}' и все товары в ней?"):
                del self.categories[name]
                self.category_listbox.delete(index)
                self.items_tree.delete(*self.items_tree.get_children())
                self.clear_item_fields()
                self.save_data()
    
    def on_category_select(self, event):
        """Обработка выбора категории"""
        selection = self.category_listbox.curselection()
        if selection:
            index = selection[0]
            self.current_category = self.category_listbox.get(index)
            self.category_title.config(text=f"Категория: {self.current_category}")
            self.load_category_items()
    
    def load_category_items(self):
        """Загрузка товаров выбранной категории"""
        self.items_tree.delete(*self.items_tree.get_children())
        
        if self.current_category in self.categories:
            for item in self.categories[self.current_category]:
                values = (
                    item.get('name', ''),
                    item.get('buy_price', ''),
                    item.get('sell_price', ''),
                    item.get('vendor', ''),
                    item.get('location', ''),
                    "✓" if item.get('icon_path') else "—"
                )
                self.items_tree.insert('', tk.END, values=values)
    
    def on_item_select(self, event):
        """Обработка выбора товара"""
        selection = self.items_tree.selection()
        if selection:
            item = self.items_tree.item(selection[0])
            values = item['values']
            
            # Найти соответствующий элемент в данных
            if self.current_category in self.categories:
                for i, data_item in enumerate(self.categories[self.current_category]):
                    if data_item.get('name') == values[0]:
                        self.current_item = i
                        self.item_name.delete(0, tk.END)
                        self.item_name.insert(0, data_item.get('name', ''))
                        self.buy_price.delete(0, tk.END)
                        self.buy_price.insert(0, data_item.get('buy_price', ''))
                        self.sell_price.delete(0, tk.END)
                        self.sell_price.insert(0, data_item.get('sell_price', ''))
                        self.vendor.delete(0, tk.END)
                        self.vendor.insert(0, data_item.get('vendor', ''))
                        self.location.delete(0, tk.END)
                        self.location.insert(0, data_item.get('location', ''))
                        
                        icon_path = data_item.get('icon_path')
                        if icon_path:
                            self.icon_label.config(text=f"Иконка: {os.path.basename(icon_path)}")
                        else:
                            self.icon_label.config(text="Иконка не выбрана")
                        
                        self.item_link.delete(0, tk.END)
                        self.item_link.insert(0, data_item.get('link', ''))
                        break
    
    def add_update_item(self):
        """Добавление или обновление товара"""
        name = self.item_name.get().strip()
        buy_price = self.buy_price.get().strip()
        sell_price = self.sell_price.get().strip()
        vendor = self.vendor.get().strip()
        location = self.location.get().strip()
        link = self.item_link.get().strip()
        
        if not name:
            messagebox.showwarning("Предупреждение", "Введите название товара!")
            return
        
        new_item = {
            'name': name,
            'buy_price': buy_price,
            'sell_price': sell_price,
            'vendor': vendor,
            'location': location,
            'link': link
        }
        
        if self.current_category:
            # Если редактируем существующий элемент
            if self.current_item is not None and self.current_item < len(self.categories[self.current_category]):
                # Сохраняем иконку, если она была
                if 'icon_path' in self.categories[self.current_category][self.current_item]:
                    new_item['icon_path'] = self.categories[self.current_category][self.current_item]['icon_path']
                
                self.categories[self.current_category][self.current_item] = new_item
            else:
                # Добавляем новый элемент
                self.categories[self.current_category].append(new_item)
            
            self.load_category_items()
            self.save_data()
            self.clear_item_fields()
    
    def delete_item(self):
        """Удаление товара"""
        if self.current_category and self.current_item is not None:
            if messagebox.askyesno("Подтверждение", "Удалить выбранный товар?"):
                if self.current_item < len(self.categories[self.current_category]):
                    del self.categories[self.current_category][self.current_item]
                    self.load_category_items()
                    self.clear_item_fields()
                    self.save_data()
    
    def add_icon(self):
        """Добавление иконки к товару"""
        if self.current_item is not None and self.current_category:
            file_path = filedialog.askopenfilename(
                title="Выберите изображение",
                filetypes=[("Изображения", "*.png *.jpg *.jpeg *.gif *.bmp")]
            )
            if file_path:
                # Сохраняем путь к иконке в текущем элементе
                if self.current_item < len(self.categories[self.current_category]):
                    self.categories[self.current_category][self.current_item]['icon_path'] = file_path
                    self.icon_label.config(text=f"Иконка: {os.path.basename(file_path)}")
                    self.load_category_items()  # Обновляем отображение
                    self.save_data()
    
    def add_link(self):
        """Добавление ссылки на товар"""
        if self.current_category and self.current_item is not None:
            link = tk.simpledialog.askstring("Ссылка на товар", "Введите ссылку:")
            if link:
                if self.current_item < len(self.categories[self.current_category]):
                    self.categories[self.current_category][self.current_item]['link'] = link
                    self.item_link.delete(0, tk.END)
                    self.item_link.insert(0, link)
                    self.save_data()
    
    def clear_item_fields(self):
        """Очистка полей ввода товара"""
        self.item_name.delete(0, tk.END)
        self.buy_price.delete(0, tk.END)
        self.sell_price.delete(0, tk.END)
        self.vendor.delete(0, tk.END)
        self.location.delete(0, tk.END)
        self.item_link.delete(0, tk.END)
        self.icon_label.config(text="Иконка не выбрана")
        self.current_item = None
    
    def save_data(self):
        """Сохранение данных в файл"""
        try:
            with open('stay_out_data.json', 'w', encoding='utf-8') as f:
                json.dump(self.categories, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные: {str(e)}")
    
    def load_data(self):
        """Загрузка данных из файла"""
        try:
            if os.path.exists('stay_out_data.json'):
                with open('stay_out_data.json', 'r', encoding='utf-8') as f:
                    self.categories = json.load(f)
                
                # Заполняем список категорий
                for category in self.categories.keys():
                    self.category_listbox.insert(tk.END, category)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {str(e)}")
            self.categories = {}
    
    def load_selected_table(self):
        """Загрузка выбранной таблицы из библиотеки"""
        # В реальной реализации здесь будет загрузка конкретной таблицы
        messagebox.showinfo("Информация", "Функция загрузки таблицы из библиотеки")
    
    def delete_saved_table(self):
        """Удаление выбранной таблицы из библиотеки"""
        messagebox.showinfo("Информация", "Функция удаления таблицы из библиотеки")
    
    def export_table(self):
        """Экспорт таблицы"""
        messagebox.showinfo("Информация", "Функция экспорта таблицы")
    
    def open_url(self, url):
        """Открытие URL в браузере"""
        import webbrowser
        webbrowser.open(url)
    
    def on_closing(self):
        """Обработка закрытия приложения"""
        self.save_data()
        self.root.destroy()

if __name__ == "__main__":
    import tkinter.simpledialog
    root = tk.Tk()
    app = StayOutMarketTracker(root)
    root.mainloop()