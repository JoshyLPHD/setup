#/bin/sh


eval "curl https://sh.rustup.rs -sSf | sh -s -- -y"
eval "rustup toolchain install nightly"
eval "rustup target install x86_64-unknown-linux-musl
eval "rustup target install x86_64-unknown-none
eval "rustup target install wasm32-unknown-unknown
eval "rustup component add rust-src"
eval "rustup target install x86_64-pc-windows-gnu "
