import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import json
import os
import time
import threading
from datetime import datetime, timedelta
import pygame
import sys

class StayOutTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stay Out Timer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize pygame mixer for sounds
        pygame.mixer.init()
        
        # Initialize alarm manager
        self.alarm_manager = AlarmManager(self)
        
        # Timer variables
        self.real_time_seconds = 0
        self.is_running = False
        self.is_paused = False
        self.game_time_ratio = 6.87  # 1 real second = 6.87 game seconds
        self.start_time = None
        self.paused_time = 0
        
        # Initialize settings dict to avoid errors
        self.settings = {}
        
        # Load settings and state
        self.load_settings()
        self.load_state()
        
        # Create UI
        self.create_widgets()
        self.update_display()
        
        # Start the timer update loop
        self.update_timer()
        
        # Bind Enter key to start timer
        self.root.bind('<Return>', self.on_enter_key)
        
        # Apply theme
        self.apply_theme()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Timer display
        display_frame = ttk.Frame(main_frame)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Real time display
        ttk.Label(display_frame, text="Реальное время:", font=("Arial", 12)).pack(anchor=tk.W)
        self.real_time_label = ttk.Label(display_frame, text="00:00:00", font=("Arial", 24, "bold"))
        self.real_time_label.pack(pady=(0, 10))
        
        # Game time display
        ttk.Label(display_frame, text="Игровое время:", font=("Arial", 12)).pack(anchor=tk.W)
        self.game_time_label = ttk.Label(display_frame, text="00:00:00", font=("Arial", 24, "bold"))
        self.game_time_label.pack(pady=(0, 10))
        
        # Time input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(input_frame, text="Изменить время", command=self.open_time_input, 
                  style="Purple.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        # Control buttons frame
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.start_button = ttk.Button(control_frame, text="Старт", command=self.start_timer, 
                                      style="Green.TButton")
        self.start_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.pause_button = ttk.Button(control_frame, text="Пауза", command=self.pause_timer, 
                                      style="Orange.TButton")
        self.pause_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.stop_button = ttk.Button(control_frame, text="Стоп", command=self.stop_timer, 
                                     style="Blue.TButton")
        self.stop_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.reset_button = ttk.Button(control_frame, text="Сброс", command=self.reset_timer, 
                                      style="Red.TButton")
        self.reset_button.pack(side=tk.LEFT, padx=(0, 5))
        
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Сохранить состояние", command=self.save_state)
        file_menu.add_command(label="Загрузить состояние", command=self.load_state)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit_app)
        
        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Настройки", menu=settings_menu)
        settings_menu.add_command(label="Параметры", command=self.open_settings)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about)
        help_menu.add_command(label="Справочник", command=self.show_help)
    
    def format_time(self, seconds):
        """Format seconds to HH:MM:SS format"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    
    def update_display(self):
        """Update the time displays"""
        real_time_str = self.format_time(self.real_time_seconds)
        game_time_seconds = self.real_time_seconds * self.game_time_ratio
        game_time_str = self.format_time(game_time_seconds)
        
        self.real_time_label.config(text=real_time_str)
        self.game_time_label.config(text=game_time_str)
    
    def update_timer(self):
        """Update the timer every second"""
        if self.is_running and not self.is_paused:
            current_time = time.time()
            elapsed = current_time - self.start_time + self.paused_time
            self.real_time_seconds = int(elapsed)
            
            # Check for alarms
            self.check_alarms()
        
        self.update_display()
        self.root.after(1000, self.update_timer)
    
    def start_timer(self):
        """Start the timer"""
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_time = time.time()
            self.paused_time = self.real_time_seconds
        else:
            self.is_paused = False
    
    def pause_timer(self):
        """Pause the timer"""
        if self.is_running:
            self.is_paused = True
    
    def stop_timer(self):
        """Stop the timer"""
        self.is_running = False
        self.is_paused = False
    
    def reset_timer(self):
        """Reset the timer to zero"""
        self.is_running = False
        self.is_paused = False
        self.real_time_seconds = 0
        self.start_time = None
        self.paused_time = 0
    
    def open_time_input(self):
        """Open the time input dialog"""
        dialog = TimeInputDialog(self.root, self)
        dialog.show()
    
    def set_time(self, hours, minutes, seconds):
        """Set the timer to a specific time"""
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.real_time_seconds = total_seconds
        if not self.is_running:
            self.start_time = time.time() - total_seconds
            self.paused_time = total_seconds
    
    def on_enter_key(self, event):
        """Handle Enter key press to start/pause timer"""
        if not self.is_running:
            self.start_timer()
        elif not self.is_paused:
            self.pause_timer()
        else:
            self.start_timer()
    
    def check_alarms(self):
        """Check if any alarms should trigger"""
        if hasattr(self, 'alarm_manager'):
            self.alarm_manager.check_alarms(self.real_time_seconds)
    
    def open_settings(self):
        """Open the settings window"""
        settings_window = SettingsWindow(self.root, self)
        settings_window.show()
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("О программе", "Stay Out Timer\nВерсия 1.0\nТаймер для игры STALKER")
    
    def show_help(self):
        """Show help dialog"""
        help_text = """
Stay Out Timer - это программа для отслеживания игрового времени в STALKER.
        
Основные функции:
- Отображение реального и игрового времени
- Соотношение времени: 1 реальная секунда = 6.87 игровых секунд
- Кнопки управления: Старт (зелёная), Пауза (оранжевая), Стоп (синяя), Сброс (красная), Изменить время (фиолетовая)
- Возможность установки будильников
- Сохранение состояния и настроек
- Настройка внешнего вида и звуков
        
Управление:
- Нажмите Enter для запуска/паузы таймера
- Используйте цифровые шкалы для установки времени
- Настройте параметры в меню "Настройки"
        """
        messagebox.showinfo("Справочник", help_text)
    
    def exit_app(self):
        """Exit the application and save state"""
        self.save_state()
        self.root.quit()
    
    def save_settings(self):
        """Save application settings to JSON file"""
        settings = {
            'game_time_ratio': self.game_time_ratio,
            'theme': getattr(self, 'current_theme', 'default'),
            'window_size': f"{self.root.winfo_width()}x{self.root.winfo_height()}",
            'alarms': getattr(self, 'alarms', []),
            'sound_settings': getattr(self, 'sound_settings', {})
        }
        
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
    
    def load_settings(self):
        """Load application settings from JSON file"""
        if os.path.exists('settings.json'):
            with open('settings.json', 'r', encoding='utf-8') as f:
                settings = json.load(f)
                self.game_time_ratio = settings.get('game_time_ratio', 6.87)
                self.current_theme = settings.get('theme', 'default')
                self.alarms = settings.get('alarms', [])
                self.sound_settings = settings.get('sound_settings', {})
        else:
            self.game_time_ratio = 6.87
            self.current_theme = 'default'
            self.alarms = []
            self.sound_settings = {}
    
    def save_state(self):
        """Save current timer state to JSON file"""
        state = {
            'real_time_seconds': self.real_time_seconds,
            'is_running': self.is_running,
            'is_paused': self.is_paused,
            'paused_time': self.paused_time
        }
        
        with open('state.json', 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    def load_state(self):
        """Load timer state from JSON file"""
        if os.path.exists('state.json'):
            with open('state.json', 'r', encoding='utf-8') as f:
                state = json.load(f)
                self.real_time_seconds = state.get('real_time_seconds', 0)
                self.is_running = state.get('is_running', False)
                self.is_paused = state.get('is_paused', False)
                self.paused_time = state.get('paused_time', 0)
                
                if self.is_running and not self.is_paused:
                    self.start_time = time.time()
    
    def apply_theme(self):
        """Apply the selected theme"""
        # Configure custom styles for buttons
        style = ttk.Style()
        
        # Green button (Start)
        style.configure("Green.TButton", 
                       foreground="white", 
                       background="#4CAF50",
                       font=("Arial", 10, "bold"))
        
        # Orange button (Pause)
        style.configure("Orange.TButton", 
                       foreground="white", 
                       background="#FF9800",
                       font=("Arial", 10, "bold"))
        
        # Blue button (Stop)
        style.configure("Blue.TButton", 
                       foreground="white", 
                       background="#2196F3",
                       font=("Arial", 10, "bold"))
        
        # Red button (Reset)
        style.configure("Red.TButton", 
                       foreground="white", 
                       background="#F44336",
                       font=("Arial", 10, "bold"))
        
        # Purple button (Change time)
        style.configure("Purple.TButton", 
                       foreground="white", 
                       background="#9C27B0",
                       font=("Arial", 10, "bold"))


class TimeInputDialog:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.dialog = None
    
    def show(self):
        """Show the time input dialog"""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("Установить время")
        self.dialog.geometry("400x300")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (
            self.parent.winfo_rootx() + 50,
            self.parent.winfo_rooty() + 50
        ))
        
        # Time selection frame
        time_frame = ttk.Frame(self.dialog)
        time_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Hours
        ttk.Label(time_frame, text="Часы:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.hour_var = tk.IntVar(value=0)
        hour_scale = ttk.Scale(time_frame, from_=0, to=23, variable=self.hour_var, 
                              orient=tk.HORIZONTAL, length=300)
        hour_scale.grid(row=1, column=0, pady=(0, 10))
        self.hour_label = ttk.Label(time_frame, text="0", font=("Arial", 12))
        self.hour_label.grid(row=2, column=0, pady=(0, 20))
        hour_scale.config(command=lambda v: self.hour_label.config(text=f"{int(float(v)):02d}"))
        
        # Minutes
        ttk.Label(time_frame, text="Минуты:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        self.minute_var = tk.IntVar(value=0)
        minute_scale = ttk.Scale(time_frame, from_=0, to=59, variable=self.minute_var, 
                                orient=tk.HORIZONTAL, length=300)
        minute_scale.grid(row=4, column=0, pady=(0, 10))
        self.minute_label = ttk.Label(time_frame, text="00", font=("Arial", 12))
        self.minute_label.grid(row=5, column=0, pady=(0, 20))
        minute_scale.config(command=lambda v: self.minute_label.config(text=f"{int(float(v)):02d}"))
        
        # Seconds
        ttk.Label(time_frame, text="Секунды:", font=("Arial", 12)).grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
        self.second_var = tk.IntVar(value=0)
        second_scale = ttk.Scale(time_frame, from_=0, to=59, variable=self.second_var, 
                                orient=tk.HORIZONTAL, length=300)
        second_scale.grid(row=7, column=0, pady=(0, 10))
        self.second_label = ttk.Label(time_frame, text="00", font=("Arial", 12))
        self.second_label.grid(row=8, column=0, pady=(0, 20))
        second_scale.config(command=lambda v: self.second_label.config(text=f"{int(float(v)):02d}"))
        
        # Buttons frame
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        ttk.Button(button_frame, text="Установить", command=self.set_time).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Отмена", command=self.dialog.destroy).pack(side=tk.LEFT)
        
        # Bind Enter key to set time
        self.dialog.bind('<Return>', lambda e: self.set_time())
    
    def set_time(self):
        """Set the time in the main application"""
        hours = self.hour_var.get()
        minutes = self.minute_var.get()
        seconds = self.second_var.get()
        
        self.app.set_time(hours, minutes, seconds)
        self.dialog.destroy()


class SettingsWindow:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.dialog = None
    
    def show(self):
        """Show the settings window"""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("Настройки")
        self.dialog.geometry("600x500")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.geometry("+%d+%d" % (
            self.parent.winfo_rootx() + 50,
            self.parent.winfo_rooty() + 50
        ))
        
        # Create notebook for tabs
        notebook = ttk.Notebook(self.dialog)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # General tab
        general_frame = ttk.Frame(notebook)
        notebook.add(general_frame, text="Общие")
        self.create_general_tab(general_frame)
        
        # Appearance tab
        appearance_frame = ttk.Frame(notebook)
        notebook.add(appearance_frame, text="Внешний вид")
        self.create_appearance_tab(appearance_frame)
        
        # Sound tab
        sound_frame = ttk.Frame(notebook)
        notebook.add(sound_frame, text="Звук")
        self.create_sound_tab(sound_frame)
        
        # Additional tab
        additional_frame = ttk.Frame(notebook)
        notebook.add(additional_frame, text="Дополнительные")
        self.create_additional_tab(additional_frame)
        
        # Buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        ttk.Button(button_frame, text="Сохранить", command=self.save_settings).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Отмена", command=self.dialog.destroy).pack(side=tk.LEFT)
    
    def create_general_tab(self, parent):
        """Create the general settings tab"""
        # Time ratio
        ttk.Label(parent, text="Соотношение игрового времени:", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(10, 5))
        ttk.Label(parent, text="1 реальная секунда =").pack(anchor=tk.W)
        
        self.ratio_var = tk.DoubleVar(value=self.app.game_time_ratio)
        ratio_frame = ttk.Frame(parent)
        ratio_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Scale(ratio_frame, from_=1.0, to=10.0, variable=self.ratio_var, 
                 orient=tk.HORIZONTAL, length=300, 
                 command=lambda v: self.ratio_value_label.config(text=f"{float(v):.2f}")).pack(side=tk.LEFT)
        
        self.ratio_value_label = ttk.Label(ratio_frame, text=f"{self.app.game_time_ratio:.2f}")
        self.ratio_value_label.pack(side=tk.LEFT, padx=(10, 0))
        
        ttk.Label(parent, text="секунд игрового времени", font=("Arial", 9)).pack(anchor=tk.W, pady=(0, 10))
    
    def create_appearance_tab(self, parent):
        """Create the appearance settings tab"""
        ttk.Label(parent, text="Настройки внешнего вида", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(10, 10))
        
        # Theme selection
        ttk.Label(parent, text="Тема оформления:", font=("Arial", 10)).pack(anchor=tk.W, pady=(0, 5))
        self.theme_var = tk.StringVar(value=getattr(self.app, 'current_theme', 'default'))
        theme_combo = ttk.Combobox(parent, textvariable=self.theme_var, 
                                  values=['default', 'dark', 'stalker'], state="readonly")
        theme_combo.pack(fill=tk.X, pady=(0, 10))
        theme_combo.set(getattr(self.app, 'current_theme', 'default'))
        
        # Color customization buttons
        color_frame = ttk.Frame(parent)
        color_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(color_frame, text="Цвет фона", 
                  command=lambda: self.choose_color('bg')).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(color_frame, text="Цвет текста", 
                  command=lambda: self.choose_color('fg')).pack(side=tk.LEFT, padx=(0, 10))
    
    def create_sound_tab(self, parent):
        """Create the sound settings tab"""
        ttk.Label(parent, text="Настройки звука", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(10, 10))
        
        # Sound enabled
        self.sound_enabled_var = tk.BooleanVar(value=self.app.sound_settings.get('enabled', True))
        sound_check = ttk.Checkbutton(parent, text="Включить звук", 
                                     variable=self.sound_enabled_var)
        sound_check.pack(anchor=tk.W, pady=(0, 10))
        
        # Sound volume
        ttk.Label(parent, text="Громкость будильника:", font=("Arial", 10)).pack(anchor=tk.W, pady=(0, 5))
        self.volume_var = tk.DoubleVar(value=self.app.sound_settings.get('volume', 0.7))
        volume_frame = ttk.Frame(parent)
        volume_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Scale(volume_frame, from_=0.0, to=1.0, variable=self.volume_var, 
                 orient=tk.HORIZONTAL, length=300,
                 command=lambda v: self.volume_value_label.config(text=f"{float(v):.0%}")).pack(side=tk.LEFT)
        
        self.volume_value_label = ttk.Label(volume_frame, text=f"{self.app.sound_settings.get('volume', 0.7):.0%}")
        self.volume_value_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Sound file selection
        ttk.Label(parent, text="Файл будильника:", font=("Arial", 10)).pack(anchor=tk.W, pady=(0, 5))
        sound_select_frame = ttk.Frame(parent)
        sound_select_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.sound_file_var = tk.StringVar(value=self.app.sound_settings.get('alarm_file', ''))
        ttk.Entry(sound_select_frame, textvariable=self.sound_file_var).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(sound_select_frame, text="Выбрать", 
                  command=self.select_sound_file).pack(side=tk.LEFT)
    
    def create_additional_tab(self, parent):
        """Create the additional settings tab"""
        ttk.Label(parent, text="Дополнительные настройки", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(10, 10))
        
        # Auto-save
        self.auto_save_var = tk.BooleanVar(value=getattr(self.app, 'settings', {}).get('auto_save', True))
        auto_save_check = ttk.Checkbutton(parent, text="Автосохранение настроек", 
                                         variable=self.auto_save_var)
        auto_save_check.pack(anchor=tk.W, pady=(0, 10))
        
        # Startup position
        ttk.Label(parent, text="Положение окна при запуске:", font=("Arial", 10)).pack(anchor=tk.W, pady=(0, 5))
        self.startup_pos_var = tk.StringVar(value=getattr(self.app, 'settings', {}).get('startup_position', 'center'))
        pos_combo = ttk.Combobox(parent, textvariable=self.startup_pos_var, 
                                values=['center', 'top-left', 'top-right', 'bottom-left', 'bottom-right'], 
                                state="readonly")
        pos_combo.pack(fill=tk.X, pady=(0, 10))
        pos_combo.set(getattr(self.app, 'settings', {}).get('startup_position', 'center'))
    
    def choose_color(self, color_type):
        """Open color chooser dialog"""
        color = colorchooser.askcolor(title=f"Выберите цвет {color_type}")[1]
        if color:
            # Store the color for later application
            if not hasattr(self.app, 'custom_colors'):
                self.app.custom_colors = {}
            self.app.custom_colors[color_type] = color
    
    def select_sound_file(self):
        """Open file dialog to select sound file"""
        file_path = filedialog.askopenfilename(
            title="Выберите звуковой файл",
            filetypes=[("Audio files", "*.wav *.mp3 *.ogg"), ("All files", "*.*")]
        )
        if file_path:
            self.sound_file_var.set(file_path)
    
    def save_settings(self):
        """Save settings to the main app"""
        # Update game time ratio
        self.app.game_time_ratio = self.ratio_var.get()
        
        # Update theme
        self.app.current_theme = self.theme_var.get()
        
        # Update sound settings
        self.app.sound_settings = {
            'enabled': self.sound_enabled_var.get(),
            'volume': self.volume_var.get(),
            'alarm_file': self.sound_file_var.get()
        }
        
        # Update additional settings
        self.app.settings = {
            'auto_save': self.auto_save_var.get(),
            'startup_position': self.startup_pos_var.get()
        }
        
        # Save to file
        self.app.save_settings()
        
        # Apply theme changes
        self.app.apply_theme()
        
        self.dialog.destroy()


class AlarmManager:
    def __init__(self, app):
        self.app = app
        self.alarms = []
    
    def add_alarm(self, time_seconds, message="Будильник"):
        """Add a new alarm"""
        alarm = {
            'time': time_seconds,
            'message': message,
            'active': True
        }
        self.alarms.append(alarm)
        self.app.alarms = self.alarms  # Update app's alarms list
    
    def remove_alarm(self, index):
        """Remove an alarm by index"""
        if 0 <= index < len(self.alarms):
            del self.alarms[index]
            self.app.alarms = self.alarms
    
    def check_alarms(self, current_time):
        """Check if any alarms should trigger"""
        triggered = []
        for i, alarm in enumerate(self.alarms):
            if alarm['active'] and current_time >= alarm['time']:
                triggered.append((i, alarm))
        
        for i, alarm in triggered:
            self.trigger_alarm(alarm)
            # Optionally remove the alarm after triggering
            # self.alarms[i]['active'] = False
    
    def trigger_alarm(self, alarm):
        """Trigger an alarm"""
        if self.app.sound_settings.get('enabled', True):
            # Play alarm sound
            alarm_file = self.app.sound_settings.get('alarm_file', '')
            if alarm_file and os.path.exists(alarm_file):
                try:
                    pygame.mixer.music.load(alarm_file)
                    pygame.mixer.music.set_volume(self.app.sound_settings.get('volume', 0.7))
                    pygame.mixer.music.play()
                except:
                    # Fallback to system beep if sound file fails
                    self.app.root.bell()
            else:
                # Default system beep
                self.app.root.bell()
        
        # Show alarm message
        messagebox.showinfo("Будильник", f"Время: {self.app.format_time(alarm['time'])}\n{alarm['message']}")


def main():
    root = tk.Tk()
    app = StayOutTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()