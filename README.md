# Command and Control (C2C) Server

This Python script provides a basic command and control (C2C) server for managing payloads. It allows you to generate payloads for different operating systems, start an HTTP server, and interact with Metasploit.

## Features

- **Payload Generation:** Create payloads for Windows, Linux, macOS, or raw formats using Metasploit.
- **HTTP Server:** Host the generated payloads using a simple HTTP server.
- **Metasploit Integration:** Automatically generate Metasploit resource files (RC files) for handling incoming connections.

## Requirements

- Python 3.x
- Metasploit Framework
- Rich Library (`rich`): Install using `pip install rich`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the C2C server:

   ```bash
   python main.py
   ```

4. Follow the on-screen prompts to configure the C2C server, select target OS, set listener port, generate payloads, and more.

## Options

The script provides the following options in an interactive menu:

- **Target OS:** Choose the target operating system (Windows, Linux, macOS, Raw).
- **Listener Port:** Set the listener port for Metasploit.
- **Payload Options:** Generate payloads for different operating systems.
- **Generate RC File:** Create a Metasploit resource file for handling connections.
- **Show Presets:** Display current configuration settings.
- **Start C2C Server:** Launch the Metasploit console with the generated RC file.
- **Quit:** Exit the script.

## Example

```bash
python main.py
```

Follow the on-screen instructions to configure the C2C server and generate payloads.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/morpheuslord/C2C-Server/blob/main/LICENSE) file for details.
