class MathLogic:
    def __init__(self):
        self.consumo_value = None
        self.nivel_ingreso_value = None

    def set_consumo(self, consumo):
        self.consumo_value = consumo

    def set_nivel_ingreso(self, nivel_ingreso):
        self.nivel_ingreso_value = nivel_ingreso        
    
    @staticmethod
    def calculate_result(nivel_ingreso, consumo):
        try:
            cargo_variable = 0
            cargo_fijo = 0
            if nivel_ingreso == 1:
                if 0 < consumo < 150:
                    cargo_variable = 67.83
                    cargo_fijo = 791
                elif 150 < consumo < 400:
                    cargo_variable = 68.13
                    cargo_fijo = 1688
                elif 400 < consumo < 600:
                    cargo_variable = 73.73
                    cargo_fijo = 5819
                elif consumo > 600:
                    cargo_variable = 80.82
                    cargo_fijo = 30054
            elif nivel_ingreso == 2:
                if 0 < consumo < 150:
                    cargo_variable = 13.10
                    cargo_fijo = 225
                elif 150 < consumo < 400:
                    cargo_variable = 13.40
                    cargo_fijo = 1688
                elif 400 < consumo < 600:
                    cargo_variable = 19.00
                    cargo_fijo = 5819
                elif consumo > 600:
                    cargo_variable = 26.10
                    cargo_fijo = 30054
            elif nivel_ingreso == 3:
                if 0 < consumo < 150:
                    cargo_variable = 12.22
                    cargo_fijo = 225
                elif 150 < consumo < 400:
                    cargo_variable = 12.52
                    cargo_fijo = 1688
                elif 400 < consumo < 600:
                    cargo_variable = 18.12
                    cargo_fijo = 5819
                elif consumo > 600:
                    cargo_variable = 25.22
                    cargo_fijo = 30054

            return consumo * cargo_variable + cargo_fijo
        except ValueError:
            return 'Invalid input'

    def calculate_result_for_current_values(self):
        if self.nivel_ingreso_value is not None and self.consumo_value is not None:
            return MathLogic.calculate_result(self.nivel_ingreso_value, self.consumo_value)
        else:
            return 'Nivel ingreso or consumo value not set'