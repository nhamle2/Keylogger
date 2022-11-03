<h1>Keylogger</h1>


<h2>Description</h2>
This project is a Python Keylogger. The program was made from the perspective of an insider threat planting a keylogger on an internal linux system to gather potential sensitive information. Upon execution, the program will begin to track all keystrokes made across the linux system. The program will output saved keystrokes into a log file for the user to view. Because this program was made from the perspective of an insider threat, the log file is not sent to a remote system or server. It is instead stored in a hidden directory called "hide" where the insider threat can later retrieve the log data and cover their tracks. This program uses the pynput input library to capture keystrokes, meaning that the target system needs to have this library installed prior to execution. Testing for this program was completed in Kali Linux.  
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python (python3)</b> 
- <b> Pynput</b>

<h2>Environments Used </h2>

- <b>Kali Linux</b>

<h2>Project walk-through:</h2>
<p align="center">
  <b>Execution:</b> <br/> <br />
  <img src="https://imgur.com/EB8VOma.png" height="40%" width="40%"/>
  <br />
  <br />
  <b>Logging keystrokes in different processes:</b> <br /> <br />
  <img src="https://imgur.com/7kU2G25.png" height="40%" width="40%" />
  <br/>
  Two different Google searches in Firefox while keylogger is running.
  <br />
  <br />
  <img src="https://imgur.com/yKZ3VUa.png" height="40%" width="40%" />
  <br/>
  Typing in Mousepad while keylogger is running.
  <br />
  <br />
  <b>Ending the keylogger:</b> <br /> <br />
  <img src="https://imgur.com/lyXEeCa.png" height="40%" width="40%" />
  <img src="https://imgur.com/KenFmux.png" height="40%" width="40%" />
  <br/>
  When the user hits the escape key, the key logger terminates. This is mainly for demonstration purposes. Ending conditions could be changed depending on the attack vector chosen by the insider threat. Once the logger program ends, the hide directory is created and the log file is moved inside
  <br/>
  <br />
  <img src="https://imgur.com/egxpcky.png" height="60%" width="60%" />
  <br />
  Contents of the log file. The keylogger writes every 14 characters to the log file. For every backspace and space, a new line is created in the log file. 
</p>

