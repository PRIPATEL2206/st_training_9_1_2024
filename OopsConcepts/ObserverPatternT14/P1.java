package OopsConcepts.ObserverPatternT14;

import java.util.ArrayList;
import java.util.List;
import java.util.Observable;
import java.util.Observer;

public class P1 {
    
}

class CusomObserver {
    private List<Observer> observers=new ArrayList<>();
    private int data=0;
    void addObserver(Observer ob){
        observers.add(ob);
    }
    void removeObserver(Observer ob ){
        observers.remove(observers.indexOf(ob));
    }

    void updateData(int d){
        data=d;

    }
    private void notifyObervers(){
        for (Observer observer : observers) {
            observer.update(observer,data);
        }
    }
}