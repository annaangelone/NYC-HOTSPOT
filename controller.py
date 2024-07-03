import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDProviders(self):
        providers = self._model._providers

        for p in providers:
            self._view._ddProvider.options.append(ft.dropdown.Option(p))
        self._view.update_page()

    def handleGrafo(self, e):
        self._view.txt_result.controls.clear()
        provider = self._view._ddProvider.value
        distanza = self._view.txt_distanza.value

        if provider is None:
            self._view.create_alert("Inserire un Provider")
            return

        try:
            distanzaF = float(distanza)

        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un valore corretto di Distanza"))
            self._view.update_page()
            return


        self._model.buildGraph(provider, distanzaF)

        for l in self._model._grafo.nodes:
            self._view._ddTarget.options.append(ft.dropdown.Option(l))

        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi."))

        self._view.update_page()


    def handleAnalisi(self, e):
        vincitori, lun = self._model.trovaVicini()

        self._view.txt_result.controls.append(ft.Text(f"Vertici con più vicini:"))

        for v in vincitori:
            self._view.txt_result.controls.append(ft.Text(f"{v}, #vicini = {lun}"))

        self._view.update_page()

    def handlePercorso(self, e):
        target = self._view._ddTarget.value
        stringa = self._view.txt_stringa.value

        if target is None:
            self._view.create_alert("Inserire un Target (t)")
            return

        if stringa is None:
            self._view.create_alert("Inserire una Stringa (s)")
            return

        self._model.getPercorso(target, stringa)