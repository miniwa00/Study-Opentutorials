package Programming;

import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Security;


public class OKJavaGOInHome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Elevator Call
		Elevator myElevator = new Elevator("Java apt 507");
		myElevator.callForUp(1);
		
		// Security off
		Security mySecurity = new Security("Java apt 507");
		mySecurity.off();
		
		// Light on
		Lighting hallLamp = new Lighting("Java apt 507 / Hall Lamp");
		hallLamp.on();
		
		Lighting floorLamp = new Lighting("Java apt 507 / floorLamp");
		floorLamp.on();
	}

}
