import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import json
import os
from PIL import Image, ImageTk
import webbrowser

class StayOutTableManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Таблица товаров для Stay Out - Harper_IDS")
        self.root.geometry("1000x700")
        
        # Установка иконки и стиля окна
        self.setup_window_style()
        
        # Переменные
        self.data_file = "data/products.json"
        self.products = {}
        self.current_category = ""
        
        # Загрузка данных
        self.load_data()
        
        # Создание интерфейса
        self.create_widgets()
        
        # Обновление списка категорий
        self.update_category_list()
        
    def setup_window_style(self):
        # Установка иконки окна (если есть)
        try:
            # Здесь можно установить иконку, если она будет создана
            pass
        except:
            pass
        
        # Цвета в стиле Сталкера
        self.bg_color = "#2d2d2d"  # Темно-серый фон
        self.fg_color = "#dcdcdc"  # Светло-серый текст
        self.accent_color = "#78c6a3"  # Зеленовато-серый акцент
        self.button_color = "#5a5a5a"  # Цвет кнопок
        self.entry_bg = "#3a3a3a"  # Фон полей ввода
        
        self.root.configure(bg=self.bg_color)
    
    def create_widgets(self):
        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Вкладка "Таблицы товаров"
        self.tables_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.tables_frame, text="Таблицы товаров")
        self.create_tables_tab()
        
        # Вкладка "Библиотека"
        self.library_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.library_frame, text="Библиотека")
        self.create_library_tab()
        
        # Вкладка "Ссылки"
        self.links_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.links_frame, text="Ссылки")
        self.create_links_tab()
        
        # Вкладка "Обучение"
        self.tutorial_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.tutorial_frame, text="Обучение")
        self.create_tutorial_tab()
    
    def create_tables_tab(self):
        # Левая часть - список категорий
        left_frame = tk.Frame(self.tables_frame, bg=self.bg_color)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        tk.Label(left_frame, text="Категории:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        # Список категорий
        self.category_listbox = tk.Listbox(left_frame, bg=self.entry_bg, fg=self.fg_color, selectbackground=self.accent_color)
        self.category_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        self.category_listbox.bind('<<ListboxSelect>>', self.on_category_select)
        
        # Кнопки управления категориями
        btn_frame = tk.Frame(left_frame, bg=self.bg_color)
        btn_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(btn_frame, text="Добавить", command=self.add_category, bg=self.button_color, fg=self.fg_color).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Удалить", command=self.delete_category, bg=self.button_color, fg=self.fg_color).pack(side=tk.LEFT, padx=2)
        
        # Правая часть - редактор товаров
        right_frame = tk.Frame(self.tables_frame, bg=self.bg_color)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Название категории
        cat_frame = tk.Frame(right_frame, bg=self.bg_color)
        cat_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(cat_frame, text="Название категории:", bg=self.bg_color, fg=self.fg_color).pack(anchor=tk.W)
        self.category_name_entry = tk.Entry(cat_frame, bg=self.entry_bg, fg=self.fg_color, state=tk.DISABLED)
        self.category_name_entry.pack(fill=tk.X, pady=2)
        
        # Список товаров
        tk.Label(right_frame, text="Товары:", bg=self.bg_color, fg=self.fg_color, font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(10, 0))
        
        # Создание таблицы товаров
        self.tree = ttk.Treeview(right_frame, columns=("name", "min_price", "my_price", "seller", "info"), show="headings", height=10)
        self.tree.heading("name", text="Название")
        self.tree.heading("min_price", text="Мин. цена покупки")
        self.tree.heading("my_price", text="Цена продажи")
        self.tree.heading("seller", text="Продавец/Место")
        self.tree.heading("info", text="Информация")
        
        # Установка ширины колонок
        self.tree.column("name", width=150)
        self.tree.column("min_price", width=100)
        self.tree.column("my_price", width=100)
        self.tree.column("seller", width=150)
        self.tree.column("info", width=200)
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Кнопки управления товарами
        btn_frame2 = tk.Frame(right_frame, bg=self.bg_color)
        btn_frame2.pack(fill=tk.X, pady=5)
        
        tk.Button(btn_frame2, text="Добавить товар", command=self.add_product, bg=self.button_color, fg=self.fg_color).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame2, text="Редактировать", command=self.edit_product, bg=self.button_color, fg=self.fg_color).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame2, text="Удалить", command=self.delete_product, bg=self.button_color, fg=self.fg_color).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame2, text="Добавить изображение", command=self.add_image, bg=self.button_color, fg=self.fg_color).pack(side=tk.LEFT, padx=2)
    
    def create_library_tab(self):
        tk.Label(self.library_frame, text="Библиотека созданных таблиц", bg=self.bg_color, fg=self.fg_color, font=("Arial", 14, "bold")).pack(pady=10)
        
        # Здесь будет список сохраненных таблиц
        tk.Label(self.library_frame, text="Здесь будут отображаться все созданные таблицы", bg=self.bg_color, fg=self.fg_color).pack(pady=20)
        
        # Кнопка загрузки таблицы
        tk.Button(self.library_frame, text="Загрузить таблицу", command=self.load_table, bg=self.button_color, fg=self.fg_color).pack(pady=10)
    
    def create_links_tab(self):
        tk.Label(self.links_frame, text="Полезные ссылки", bg=self.bg_color, fg=self.fg_color, font=("Arial", 14, "bold")).pack(pady=10)
        
        links = [
            ("Официальная страница игры в Steam", "https://store.steampowered.com/app/1180380/Stay_Out/"),
            ("Википедия игры Stay Out", "https://so-wiki.ru/"),
            ("Мой профиль в Steam", "https://steamcommunity.com/id/Harper_IDS/")
        ]
        
        for text, url in links:
            btn = tk.Button(self.links_frame, text=text, command=lambda u=url: webbrowser.open_new(u), 
                           bg=self.button_color, fg=self.fg_color, width=40, height=2)
            btn.pack(pady=5)
    
    def create_tutorial_tab(self):
        tk.Label(self.tutorial_frame, text="Обучение использованию", bg=self.bg_color, fg=self.fg_color, font=("Arial", 14, "bold")).pack(pady=10)
        
        tutorial_text = """
        1. Перейдите на вкладку "Таблицы товаров"
        
        2. Создайте новую категорию товаров:
           - Нажмите "Добавить" в списке категорий
           - Введите название категории (например, "Грибы")
        
        3. Добавьте товары в категорию:
           - Выберите категорию из списка
           - Нажмите "Добавить товар"
           - Заполните поля:
             * Название товара
             * Минимальная цена покупки
             * Ваша цена продажи
             * Продавец/Место продажи
             * Дополнительная информация
        
        4. Добавьте изображение для товара:
           - Выберите товар в таблице
           - Нажмите "Добавить изображение"
        
        5. Все данные автоматически сохраняются
        
        6. Вкладка "Библиотека" содержит все созданные таблицы
        
        7. Вкладка "Ссылки" содержит полезные ресурсы по игре
        """
        
        text_widget = tk.Text(self.tutorial_frame, wrap=tk.WORD, bg=self.entry_bg, fg=self.fg_color, height=20)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        text_widget.insert(tk.END, tutorial_text)
        text_widget.config(state=tk.DISABLED)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.products = json.load(f)
            except:
                self.products = {}
        else:
            self.products = {}
    
    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.products, f, ensure_ascii=False, indent=2)
    
    def update_category_list(self):
        self.category_listbox.delete(0, tk.END)
        for category in self.products.keys():
            self.category_listbox.insert(tk.END, category)
    
    def on_category_select(self, event):
        selection = self.category_listbox.curselection()
        if selection:
            self.current_category = self.category_listbox.get(selection[0])
            self.category_name_entry.config(state=tk.NORMAL)
            self.category_name_entry.delete(0, tk.END)
            self.category_name_entry.insert(0, self.current_category)
            self.category_name_entry.config(state=tk.DISABLED)
            self.update_product_list()
    
    def update_product_list(self):
        # Очистка таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Заполнение таблицы
        if self.current_category in self.products:
            for product in self.products[self.current_category]:
                self.tree.insert("", tk.END, values=(
                    product.get("name", ""),
                    product.get("min_price", ""),
                    product.get("my_price", ""),
                    product.get("seller", ""),
                    product.get("info", "")
                ))
    
    def add_category(self):
        category_name = simpledialog.askstring("Новая категория", "Введите название категории:")
        if category_name and category_name.strip():
            if category_name not in self.products:
                self.products[category_name] = []
                self.save_data()
                self.update_category_list()
                messagebox.showinfo("Успех", f"Категория '{category_name}' создана!")
            else:
                messagebox.showwarning("Ошибка", "Категория с таким названием уже существует!")
    
    def delete_category(self):
        if self.current_category:
            if messagebox.askyesno("Подтверждение", f"Вы действительно хотите удалить категорию '{self.current_category}'?"):
                del self.products[self.current_category]
                self.save_data()
                self.update_category_list()
                self.current_category = ""
                # Очистка таблицы товаров
                for item in self.tree.get_children():
                    self.tree.delete(item)
                self.category_name_entry.config(state=tk.NORMAL)
                self.category_name_entry.delete(0, tk.END)
                self.category_name_entry.config(state=tk.DISABLED)
                messagebox.showinfo("Успех", f"Категория '{self.current_category}' удалена!")
        else:
            messagebox.showwarning("Ошибка", "Сначала выберите категорию для удаления!")
    
    def add_product(self):
        if not self.current_category:
            messagebox.showwarning("Ошибка", "Сначала выберите категорию!")
            return
        
        # Создание диалогового окна для добавления товара
        dialog = AddProductDialog(self.root, self.add_product_callback)
    
    def add_product_callback(self, product_data):
        self.products[self.current_category].append(product_data)
        self.save_data()
        self.update_product_list()
    
    def edit_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите товар для редактирования!")
            return
        
        # Получение индекса выбранного элемента
        item_idx = self.tree.index(selected_item[0])
        
        # Открытие диалога редактирования
        product_data = self.products[self.current_category][item_idx]
        dialog = EditProductDialog(self.root, product_data, self.edit_product_callback, item_idx)
    
    def edit_product_callback(self, product_data, item_idx):
        self.products[self.current_category][item_idx] = product_data
        self.save_data()
        self.update_product_list()
    
    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите товар для удаления!")
            return
        
        if messagebox.askyesno("Подтверждение", "Вы действительно хотите удалить выбранный товар?"):
            item_idx = self.tree.index(selected_item[0])
            del self.products[self.current_category][item_idx]
            self.save_data()
            self.update_product_list()
    
    def add_image(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите товар для добавления изображения!")
            return
        
        file_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Изображения", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        
        if file_path:
            # В реальной реализации здесь будет сохранение изображения
            messagebox.showinfo("Изображение", f"Изображение добавлено: {file_path}")
    
    def load_table(self):
        file_path = filedialog.askopenfilename(
            title="Загрузить таблицу",
            filetypes=[("JSON файлы", "*.json"), ("Все файлы", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    new_data = json.load(f)
                
                # Подтверждение загрузки
                if messagebox.askyesno("Подтверждение", "Загрузить таблицу? Это заменит текущие данные."):
                    self.products = new_data
                    self.save_data()
                    self.update_category_list()
                    messagebox.showinfo("Успех", "Таблица загружена!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить таблицу: {str(e)}")

class AddProductDialog:
    def __init__(self, parent, callback):
        self.callback = callback
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Добавить товар")
        self.dialog.geometry("400x300")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Центрирование окна
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        
        self.create_widgets()
    
    def create_widgets(self):
        frame = tk.Frame(self.dialog, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Поля ввода
        tk.Label(frame, text="Название товара:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_entry = tk.Entry(frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=2)
        
        tk.Label(frame, text="Мин. цена покупки:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.min_price_entry = tk.Entry(frame, width=40)
        self.min_price_entry.grid(row=1, column=1, pady=2)
        
        tk.Label(frame, text="Цена продажи:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.my_price_entry = tk.Entry(frame, width=40)
        self.my_price_entry.grid(row=2, column=1, pady=2)
        
        tk.Label(frame, text="Продавец/Место:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.seller_entry = tk.Entry(frame, width=40)
        self.seller_entry.grid(row=3, column=1, pady=2)
        
        tk.Label(frame, text="Информация:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.info_text = tk.Text(frame, width=30, height=4)
        self.info_text.grid(row=4, column=1, pady=2)
        
        # Кнопки
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="Сохранить", command=self.save_product).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Отмена", command=self.dialog.destroy).pack(side=tk.LEFT, padx=5)
    
    def save_product(self):
        product_data = {
            "name": self.name_entry.get(),
            "min_price": self.min_price_entry.get(),
            "my_price": self.my_price_entry.get(),
            "seller": self.seller_entry.get(),
            "info": self.info_text.get("1.0", tk.END).strip()
        }
        
        # Проверка обязательных полей
        if not product_data["name"]:
            messagebox.showwarning("Ошибка", "Введите название товара!")
            return
        
        self.callback(product_data)
        self.dialog.destroy()

class EditProductDialog:
    def __init__(self, parent, product_data, callback, item_idx):
        self.callback = callback
        self.item_idx = item_idx
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Редактировать товар")
        self.dialog.geometry("400x300")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Центрирование окна
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        
        self.create_widgets(product_data)
    
    def create_widgets(self, product_data):
        frame = tk.Frame(self.dialog, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Поля ввода
        tk.Label(frame, text="Название товара:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_entry = tk.Entry(frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=2)
        self.name_entry.insert(0, product_data.get("name", ""))
        
        tk.Label(frame, text="Мин. цена покупки:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.min_price_entry = tk.Entry(frame, width=40)
        self.min_price_entry.grid(row=1, column=1, pady=2)
        self.min_price_entry.insert(0, product_data.get("min_price", ""))
        
        tk.Label(frame, text="Цена продажи:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.my_price_entry = tk.Entry(frame, width=40)
        self.my_price_entry.grid(row=2, column=1, pady=2)
        self.my_price_entry.insert(0, product_data.get("my_price", ""))
        
        tk.Label(frame, text="Продавец/Место:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.seller_entry = tk.Entry(frame, width=40)
        self.seller_entry.grid(row=3, column=1, pady=2)
        self.seller_entry.insert(0, product_data.get("seller", ""))
        
        tk.Label(frame, text="Информация:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.info_text = tk.Text(frame, width=30, height=4)
        self.info_text.grid(row=4, column=1, pady=2)
        self.info_text.insert("1.0", product_data.get("info", ""))
        
        # Кнопки
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="Сохранить", command=self.save_product).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Отмена", command=self.dialog.destroy).pack(side=tk.LEFT, padx=5)
    
    def save_product(self):
        product_data = {
            "name": self.name_entry.get(),
            "min_price": self.min_price_entry.get(),
            "my_price": self.my_price_entry.get(),
            "seller": self.seller_entry.get(),
            "info": self.info_text.get("1.0", tk.END).strip()
        }
        
        # Проверка обязательных полей
        if not product_data["name"]:
            messagebox.showwarning("Ошибка", "Введите название товара!")
            return
        
        self.callback(product_data, self.item_idx)
        self.dialog.destroy()

def main():
    root = tk.Tk()
    app = StayOutTableManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()