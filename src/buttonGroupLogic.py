class buttonGroupLogic:
    def __init__(self, source_buttons, target_buttons):
        self.source_buttons = source_buttons  # Botões checkable (add, edit, remove)
        self.target_buttons = target_buttons  # Botões não checkable (back, save)
        self.last_clicked_source = None       # Armazena o último botão source clicado

        # Conectar clicks dos source_buttons
        for button in self.source_buttons:
            button.clicked.connect(lambda checked, btn=button: self.handle_source_click(btn))

        # Conectar clicks dos target_buttons
        for button in self.target_buttons:
            button.clicked.connect(self.handle_target_click)

    def handle_source_click(self, clicked_button):
        # Desmarca todos os outros botões source
        for button in self.source_buttons:
            if button != clicked_button:
                button.setChecked(False)
        
        # Se o botão foi marcado
        if clicked_button.isChecked():
            self.last_clicked_source = clicked_button
            # Desativa todos os source_buttons
            for button in self.source_buttons:
                button.setEnabled(False)
            # Ativa os target_buttons
            for button in self.target_buttons:
                button.setEnabled(True)
        else:
            # Se foi desmarcado, mantém target_buttons desativados
            for button in self.target_buttons:
                button.setEnabled(False)

    def handle_target_click(self):
        # Reativa todos os source_buttons
        for button in self.source_buttons:
            button.setEnabled(True)
            button.setChecked(False)  # Garante que todos estão desmarcados
        
        # Desativa todos os target_buttons
        for button in self.target_buttons:
            button.setEnabled(False)
        
        # Reseta a referência do último botão clicado
        self.last_clicked_source = None