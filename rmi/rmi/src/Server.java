import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server implements MyInterface {

    public Server() throws RemoteException {
        super();
    }

    @Override
    public String sayHello(String name) throws RemoteException {
        return "Hello, " + name + "!";
    }

    public static void main(String[] args) {
        try {
            // Cria uma instância do objeto servidor
            Server server = new Server();

            // Exporta o objeto para o RMI registry, tornando-o acessível remotamente
            Client stub = (Client) UnicastRemoteObject.exportObject(server, 0);

            // Obtém o registro RMI local e o vincula ao objeto remoto
            Registry registry = LocateRegistry.getRegistry();
            registry.rebind("MyInterface", stub);

            System.out.println("Servidor RMI iniciado.");
        } catch (Exception e) {
            System.err.println("Erro no servidor RMI: " + e.toString());
            e.printStackTrace();
        }
    }
}
