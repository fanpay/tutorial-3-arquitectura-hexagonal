class Consulta:
    """Clase base para representar una consulta."""
    ...

class ManejadorConsulta:
    """Interfaz para los manejadores de consultas."""
    
    def ejecutar(self, consulta: Consulta):
        """Ejecuta la consulta especificada."""
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
