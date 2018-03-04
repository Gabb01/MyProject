package server;

import javax.ws.rs.GET;
import javax.ws.rs.Path;

@Path("r1")
public class firstResource {
	
	@GET
	public String hello() 
	{
		return "Hello String";
	}
}
