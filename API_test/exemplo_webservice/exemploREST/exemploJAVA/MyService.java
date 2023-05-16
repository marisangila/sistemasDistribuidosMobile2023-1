@Path("/Add")
public class MyService {
 
    @GET
    @Path("/{a}/{b}")
    @Produces(MediaType.APPLICATION_JSON)
    public int add(@PathParam("a") int a, @PathParam("b") int b)
    {
        return a + b;
    }
 
}
