package OopsConcepts.FactoryMethodT35;

public class p2 {
    public static void main(String[] args) {
        VehiclesFactory vf =new VehiclesFactory();
        Car c=vf.createCar("Swift");
        Bike b=vf.createBike("Pulser");
    }
}
