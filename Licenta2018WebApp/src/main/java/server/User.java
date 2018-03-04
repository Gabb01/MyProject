package server;

import java.io.Serializable;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
@XmlRootElement(name = "user")
public class User implements Serializable {

   private static final long serialVersionUID = 1L;
   private int id;
   private String nume;
   private String oras;

   public User(){}

   public User(int id, String nume, String oras){
      this.id = id;
      this.nume = nume;
      this.oras = oras;
   }

   public int getId() {
      return id;
   }
   @XmlElement
   public void setId(int id) {
      this.id = id;
   }
   public String getName() {
      return nume;
   }
   @XmlElement
      public void setName(String nume) {
      this.nume = nume;
   }
   public String getCity() {
      return oras;
   }
   @XmlElement
   public void setCity(String oras) {
      this.oras = oras;
   }	

   @Override
   public boolean equals(Object object){
      if(object == null){
         return false;
      }else if(!(object instanceof User)){
         return false;
      }else {
         User user = (User)object;
         if(id == user.getId()
            && nume.equals(user.getName())
            && oras.equals(user.getCity())
         ){
            return true;
         }			
      }
      return false;
   }	
}
