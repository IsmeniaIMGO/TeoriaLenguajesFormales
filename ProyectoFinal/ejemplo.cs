using System;

namespace CalculadoraBasica
{
    class Program
    {
        static void Main(string[] args)
        {
            ñ

            if (args.Length == 0)
            {
                Console.WriteLine("Por favor, ingrese los números y el operador.");
                return;
            }
            
            double num1 = 10.5;
            double num2 = 5.2;
            char operador = '+';
            double resultado = 0;

            switch (operador)
            {
                case '+':
                    resultado = num1 + num2;
                    break;
                case '-':
                    resultado = num1 - num2;
                    break;
                case '*':
                    resultado = num1 * num2;
                    break;
                case '/':
                    if (num2 != 0)
                    {
                        resultado = num1 / num2;
                    }
                    else
                    {
                        Console.WriteLine("Error: División por cero");
                    }
                    break;
                default:
                    Console.WriteLine("Operador no válido");
                    break;
            }

            Console.WriteLine("Resultado: " + resultado);
        }
    }
}
