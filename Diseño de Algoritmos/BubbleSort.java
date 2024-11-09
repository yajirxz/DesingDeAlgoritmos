import java.util.Arrays;

class BubbleSort {
    void bubbleSort(int array[]) {
        int size = array.length;

        // Ejecutar el bucle dos veces: uno para recorrer la lista y otro para comparar los números
        for (int i = 0; i < size - 1; i++) {

            // Se genera un registro de los intercambios
            boolean swapped = true;
            for (int j = 0; j < size - i - 1; j++) {

                if (array[j] > array[j + 1]) {

                    // Intercambio
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;

                    swapped = false;
                }
            }

            // Si no ha habido intercambio en la última comparación, entonces la lista ya está ordenado.
            if (swapped == true)
                break;
        }
    }

    public static void main(String args[]) {
        //Donde está la lista desordenada
        int[] data = { 9, 4, 3, 6, 1, 8, 7, 2, 5 };
        BubbleSort bs = new BubbleSort();
        bs.bubbleSort(data);
        System.out.println("La lista se ha ordenado");
        System.out.println(Arrays.toString(data));
    }}
//Complejidad temporal: O(n^2)
//Complejidad espacial: 0(1)