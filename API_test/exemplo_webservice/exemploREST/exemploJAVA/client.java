import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

public class AddClient {

    public static void main(String[] args) {
        Client client = ClientBuilder.newClient();
        WebTarget target = client.target("http://localhost:8080/Add/add/10/20");
        int result = target.request(MediaType.APPLICATION_JSON).get(Integer.class);
        System.out.println("Resultado: " + result);
    }
}
