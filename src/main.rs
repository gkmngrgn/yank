use structopt::StructOpt;
use yank::{
    client::make_request,
    server::run_server
};

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
    match opt.cmd {
        Some(Command::Server { daemon }) => {
            run_server();
        }
        Some(Command::List { machine }) => {
            make_request();
        }
        None => {
            println!("{:#?}", opt);
        }
    }
}
