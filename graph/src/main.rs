use macroquad::prelude::*;

#[macroquad::main("Graph")]
async fn main() {
    loop {
        clear_background(BLACK);

        draw_line(
            0.0,
            screen_height() / 2.0,
            screen_width(),
            screen_height() / 2.0,
            1.0,
            WHITE,
        );
        draw_line(
            screen_width() / 2.0,
            0.0,
            screen_width() / 2.0,
            screen_height(),
            1.0,
            WHITE,
        );
        for i in -300..300 {
            let x: f32 = i as f32 / 100.0;
            let y: f32 = fun(x);
            draw_circle(
                x * screen_width() / 6. + screen_width() / 2.0,
                y * screen_height() / 6. + screen_height() / 2.0,
                1.0,
                WHITE,
            );
        }

        next_frame().await
    }
}

fn fun(x: f32) -> f32 {
    return (x.abs() * 2. - 3.)
        * (x.abs() * 2. - 2.)
        * (x.abs() * 2. - 4.)
        * x.abs()
        * 2.
        * x.abs().sqrt()
        / 12.;
}
