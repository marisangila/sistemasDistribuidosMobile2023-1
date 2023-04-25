import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;

public class AddClient {

    public static void main(String[] args) throws Exception {
        URL url = new URL("http://localhost:8080/Add?wsdl");
        QName qname = new QName("http://example.com/", "AddService");
        Service service = Service.create(url, qname);
        Add add = service.getPort(Add.class);
        int result = add.add(10, 20);
        System.out.println("Resultado: " + result);
    }
}
