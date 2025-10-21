import com.fazecast.jSerialComm.SerialPort;
import java.util.Scanner;

public class LeerMicrobit {
    public static void main(String[] args) {
        SerialPort puerto = SerialPort.getCommPort("COM3"); // Ajustar el puerto
        puerto.setBaudRate(115200);
        puerto.openPort();

        if (puerto.isOpen()) {
            System.out.println("Conectado al micro:bit");
            Scanner scanner = new Scanner(puerto.getInputStream());
            while (scanner.hasNextLine()) {
                String linea = scanner.nextLine();
                System.out.println("Dato recibido: " + linea);
            }
            scanner.close();
            puerto.closePort();
        } else {
            System.out.println("No se pudo abrir el puerto");
        }
    }
}
