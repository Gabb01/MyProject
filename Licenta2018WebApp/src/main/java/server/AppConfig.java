package server;

import java.util.HashSet;
import java.util.Set;

import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;

@ApplicationPath("v1")
public class AppConfig extends Application {

	private Set<Class<?>> resources = new HashSet<>();
	
	public AppConfig() {
		resources.add(firstResource.class);
		resources.add(RESTUtilizator.class);
	}
	
	@Override
	public Set<Class<?>> getClasses() {
		return resources;
	}
	
	

}
