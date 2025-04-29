package problems.fizzbuzz.java.jayce_cripe;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class FizzBuzzServer {

    private static String fizzBuzzResult = "No number provided.";

    public static void main(String[] args) throws IOException {
        if (args.length == 0) {
            System.out.println("Please provide a number when starting the server.");
            System.exit(1);
        }

        try {
            int number = Integer.parseInt(args[0]);
            fizzBuzzResult = generateFizzBuzzOutput(number);
        } catch (NumberFormatException e) {
            System.out.println("Invalid number: " + args[0]);
            System.exit(1);
        }

        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/fizzbuzz", FizzBuzzServer::handleRequest);
        server.start();
        System.out.println("Server started at http://localhost:8000/fizzbuzz");
    }

    private static void handleRequest(HttpExchange exchange) throws IOException {
        String response = fizzBuzzResult;
        exchange.sendResponseHeaders(200, response.length());
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }

    private static String generateFizzBuzzOutput(int n) {
    StringBuilder output = new StringBuilder();
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            output.append("BobCat");
        } else if (i % 3 == 0) {
            output.append("Bob");
        } else if (i % 5 == 0) {
            output.append("Cat");
        } else {
            output.append(i);
        }
        output.append("\n");
    }
    return output.toString().trim();
}

}
