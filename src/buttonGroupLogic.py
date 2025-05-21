class buttonGroupLogic:
    def __init__(self, source_buttons, target_buttons):
        self.source_buttons = source_buttons  # Botões não checkable agora
        self.target_buttons = target_buttons
        self.active_source = None  # Botão source ativo no momento

        for button in self.source_buttons:
            button.clicked.connect(lambda _, btn=button: self.handle_source_click(btn))

        for button in self.target_buttons:
            button.clicked.connect(self.handle_target_click)

    def handle_source_click(self, clicked_button):
        
        # Desativa todos os outros source_buttons, menos o clicado
        for button in self.source_buttons:
            
            if button != clicked_button:
                button.setEnabled(False)
            else:
                button.setEnabled(True)  # Garante que ele mesmo fique ativo
        
        # Ativa os target_buttons
        for button in self.target_buttons:
            button.setEnabled(True)
        
        # Guarda qual botão está ativo
        self.active_source = clicked_button

    def handle_target_click(self):
        # Reativa todos os source_buttons
        for button in self.source_buttons:
            button.setEnabled(True)
        
        # Desativa todos os target_buttons
        for button in self.target_buttons:
            button.setEnabled(False)
        
        # Reseta referência
        self.active_source = None
