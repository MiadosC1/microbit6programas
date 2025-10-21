#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>

int main() {
    std::ifstream puerto("/dev/ttyACM0"); // Cambia a COM3 en Windows
    if (!puerto.is_open()) {
        std::cerr << "No se pudo abrir el puerto\n";
        return 1;
    }

    std::string linea;
    while (std::getline(puerto, linea)) {
        std::cout << "Dato recibido: " << linea << std::endl;
    }

    puerto.close();
    return 0;
}
