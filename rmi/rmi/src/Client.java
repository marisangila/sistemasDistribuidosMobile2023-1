import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Client extends Remote {
    public String sayHello(String name) throws RemoteException;
}

