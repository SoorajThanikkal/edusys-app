/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package constructors;
import java.io.*;

class Area
{
    double area;
    
    Area(float x)
    {
        area=x*x;
    }
    
    Area(float x,float y)
    {
        area=x*y;
    }
    
    Area(float x,float y, float z)
    {
        double s;
        s=(x+y+z)/2.0;
        area=Math.sqrt(s*(s-x)*(s-y)*(s-z));   
    }
    void display()
    {
        System.out.println("Area is"+area);
    }
}
/**
 *
 * @author user
 */
public class Constructors {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        
        float a,b,c;
        System.out.println("Enter side of square:");
        a=Float.parseFloat(br.readLine());
        Area Square=new Area(a);
        Square.display();
        
        System.out.println("Enter length and breadth of rectangle:");
        a=Float.parseFloat(br.readLine());
        b=Float.parseFloat(br.readLine());
        Area Rectangle=new Area(a,b);
        Rectangle.display();
        
        System.out.println("Enter three sides of the triangle:");
        a=Float.parseFloat(br.readLine());
        b=Float.parseFloat(br.readLine());
        c=Float.parseFloat(br.readLine());
        Area Triangle=new Area(a,b,c);
        Triangle.display();
    }
    
}
