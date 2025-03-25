import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class FizzBuzzTest {
    @Test
    public void testNoArguments() {
        // Redirect standard output to capture prints
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));
        
        // Run main with no arguments
        FizzBuzz.main(new String[]{});
        
        // Restore the original System.out
        System.setOut(originalOut);
        
        // Expected output when no arguments are provided.
        String expectedOutput = "Please provide a number as an argument." + System.lineSeparator();
        assertEquals(expectedOutput, outContent.toString());
    }
    
    @Test
    public void testFizzBuzzOutput() {
        // Redirect standard output to capture prints
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));
        
        // Run main with an argument of 16
        FizzBuzz.main(new String[]{"16"});
        
        // Restore the original System.out
        System.setOut(originalOut);
        
        // Expected output for n = 16
        String expectedOutput = 
            "Input: n = 16" + System.lineSeparator() +
            "1" + System.lineSeparator() +
            "2" + System.lineSeparator() +
            "Bob" + System.lineSeparator() +
            "4" + System.lineSeparator() +
            "Cat" + System.lineSeparator() +
            "Bob" + System.lineSeparator() +
            "7" + System.lineSeparator() +
            "8" + System.lineSeparator() +
            "Bob" + System.lineSeparator() +
            "Cat" + System.lineSeparator() +
            "11" + System.lineSeparator() +
            "Bob" + System.lineSeparator() +
            "13" + System.lineSeparator() +
            "14" + System.lineSeparator() +
            "BobCat" + System.lineSeparator() +
            "16" + System.lineSeparator();
            
        assertEquals(expectedOutput, outContent.toString());
    }
}
