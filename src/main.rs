use structopt::StructOpt;

#[derive(StructOpt, Debug)]
struct Opt {
    #[structopt(subcommand)]
    cmd: Option<Command>,
}

#[derive(StructOpt, Debug)]
#[structopt(name = "yank")]
enum Command {
    Server {
        #[structopt(short)]
        daemon: bool,
    },
    List {
        #[structopt(short)]
        machine: Option<String>,
    },
}

fn main() {
    let opt = Opt::from_args();
    println!("{:#?}", opt);
}
