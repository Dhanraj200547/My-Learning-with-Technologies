// Define a class
class Car {
    // Fields (properties)
    String brand;
    String color;
    int year;

    // Constructor (to initialize objects)
    Car(String brand, String color, int year) {
        this.brand = brand;
        this.color = color;
        this.year = year;
    }

    // Method (behavior)
    void displayDetails() {
        System.out.println("Brand: " + brand);
        System.out.println("Color: " + color);
        System.out.println("Year: " + year);
    }
}

// oops class to demonstrate objects
public class oops {
    public static void oops(String[] args) {
        // Create an object of the Car class
        Car car1 = new Car("Tesla", "Red", 2023);
        Car car2 = new Car("BMW", "Blue", 2020);

        // Call method on the object
        System.out.println("Car 1 Details:");
        car1.displayDetails();

        System.out.println("\nCar 2 Details:");
        car2.displayDetails();
    }
}
