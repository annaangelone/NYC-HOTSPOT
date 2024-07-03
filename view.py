import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "ESAME 18/01/2023 NYC-Hotspots"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME 18/01/2023 NYC-Hotspots", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddProvider = ft.Dropdown(label="Provider (p)", width=200, alignment=ft.alignment.top_left)
        self._controller.fillDDProviders()

        self._btnGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleGrafo)

        row1 = ft.Row([ft.Container(self._ddProvider, width=250), ft.Container(self._btnGrafo, width=250)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW with some controls
        # text field for the name
        self.txt_distanza = ft.TextField(
            label="Distanza (x)",
            width=200,
            hint_text="Inserisci una distanza"
        )

        # button for the "hello" reply
        self.btn_analisi = ft.ElevatedButton(text="Analisi Grafo", on_click=self._controller.handleAnalisi)
        row2 = ft.Row([ft.Container(self.txt_distanza, width=250), ft.Container(self.btn_analisi, width=250)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.txt_stringa = ft.TextField(
            label="Stringa (x)",
            width=200,
            hint_text="Inserisci una stringa"
        )

        self.btn_percorso = ft.ElevatedButton(text="Calcola Percorso", on_click=self._controller.handlePercorso)

        self._ddTarget = ft.Dropdown(label="Target (t)", width=200, alignment=ft.alignment.top_left)

        row3 = ft.Row([ft.Container(self.txt_stringa, width=250), ft.Container(self.btn_percorso, width=250)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        row4 = ft.Row([ft.Container(self._ddTarget, width=250), ft.Container(None, width=250)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
