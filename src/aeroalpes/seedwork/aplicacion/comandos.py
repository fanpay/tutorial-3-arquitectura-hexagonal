class Comando:
    """Clase base para representar un comando."""
    ...

class ManejadorComando:
    """Interfaz para los manejadores de comandos."""
    
    def ejecutar(self, comando: Comando):
        """Ejecuta el comando especificado."""
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
