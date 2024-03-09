import java.util.Random;
public class random_number {
    public static void main(String[]args)
    {
        A t=new A();
        t.rand();
    }

}
class A
{
    void rand()
    {
        Random r=new Random();
        int num= r.nextInt(10)+1;
        System.out.println("The Random number is  "+num);
        if(num%4==0)
        {
            System.out.println("Its divisible " +num);
            return;
        }
        else {
            rand();
        }
    }
}