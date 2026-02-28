use std::fs::OpenOptions;
use std::io::prelude::*;

fn main() {
    let ruta_mdb = r"C:\CAMASOTS_V1\MDB\MDB_05_PROGRAMACION.csv";
    let mut file = OpenOptions::new()
        .append(true)
        .open(ruta_mdb)
        .expect("NO SE PUDO ABRIR LA MDB");

    writeln!(file, "003;UPGRADE;KERNEL_RUST_ESTABLE;ACTIVO;2026-02-23").unwrap();
    println!("PODER RUST ACTIVADO");
}
