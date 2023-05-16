import org.apache.axis2.AxisFault;
import org.apache.axis2.context.MessageContext;
import org.apache.axis2.transport.http.HTTPConstants;

public class MyService {

    public int Add(int a, int b) throws AxisFault {
        // obtém o contexto da mensagem para acessar o cabeçalho SOAPAction
        MessageContext messageContext = MessageContext.getCurrentMessageContext();

        // verifica se a solicitação contém o cabeçalho SOAPAction adequado
        String soapAction = (String) messageContext.getProperty(HTTPConstants.HEADER_SOAP_ACTION);
        if (!"http://example.com/myservice/Add".equals(soapAction)) {
            throw new AxisFault("SOAPAction não suportado");
        }

        // realiza a soma e retorna o resultado
        int result = a + b;
        return result;
    }
}
