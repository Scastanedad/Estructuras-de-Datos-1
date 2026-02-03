package archivos1;
import java.io.*;

public class Archivos1 {

    public static void main(String[] args) {

        String linea;
        File Archivo = new File("/Users/sneda/Proyectos/PythonYT/Python01/Manejo de datos/ftexts/nombres.txt");

        FileReader lectorArchivo = null;
        BufferedReader BufferArchivo = null;

        try {
            lectorArchivo = new FileReader(Archivo);
            BufferArchivo = new BufferedReader(lectorArchivo);

            while ((linea = BufferArchivo.readLine()) != null) {
                System.out.println(linea);
            }
            BufferArchivo.close();
        } catch (FileNotFoundException e) {
            System.out.println("Archivo no encontrado");
        } catch (IOException e) {
            System.out.println("Error al leer el archivo");
        }
    }
}
