use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use serde::Deserialize;

#[derive(Deserialize)]
struct QueryParams {
    bound: i32,
}

fn bobcat(number: &i32) -> String {
    if number % 3 == 0 && number % 5 == 0 {
        "BobCat".to_string()
    } else if number % 3 == 0 {
        "Bob".to_string()
    } else if number % 5 == 0 {
        "Cat".to_string()
    } else {
        number.to_string()
    }
}

async fn query_handler(query: web::Query<QueryParams>) -> impl Responder {
    let bound = query.bound;
    let mut result = String::new();

    for current in 1..=bound {
        result.push_str(&bobcat(&current));
        result.push('\n');
    }

    HttpResponse::Ok().content_type("text/plain").body(result)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Starting server at 127.0.0.1/8080");
    println!("Try visting the url: http://localhost:8080/?bound=15");
    println!("Or run the command: curl 'http://localhost:8080/?bound=15'");
    HttpServer::new(|| {
        App::new().route("/", web::get().to(query_handler))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
