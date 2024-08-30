<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
</head>
<body>

<h1>PDF to Audiobook Converter</h1>

<h2>🚀 Overview</h2>
<p>The <strong>PDF to Audiobook Converter</strong> is a tool that transforms your PDF documents into audiobooks. It uses text-to-speech (TTS) technology to let you listen to your favorite books, articles, or any other PDFs while on the go.</p>

<h2>🎯 Features</h2>
<ul>
    <li><strong>PDF to Audio Conversion</strong>: Convert any PDF into an audiobook.</li>
    <li><strong>Multi-Language Support</strong>: Supports multiple languages for conversion.</li>
    <li><strong>Customizable Voices</strong>: Choose different voice options and adjust the speech rate.</li>
    <li><strong>Batch Processing</strong>: Convert multiple PDF files at once.</li>
    <li><strong>Output Formats</strong>: Save audiobooks in popular formats like MP3.</li>
</ul>

<h2>🛠️ Installation</h2>
<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>Pip (Python package manager)</li>
</ul>

<h3>Install Dependencies</h3>
<p>First, clone the repository:</p>
<pre><code>git clone https://github.com/your-username/pdf-to-audiobook-converter.git
cd pdf-to-audiobook-converter</code></pre>

<p>Then, install the required Python packages:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>🚀 Usage</h2>
<p>To convert your PDFs to audiobooks, follow these steps:</p>
<ol>
    <li>Place your PDF files in the <code>input_pdfs</code> directory.</li>
    <li>Run the conversion script:</li>
</ol>
<pre><code>python convert_to_audio.py --input input_pdfs --output output_audiobooks --voice male --language en --rate 1.0</code></pre>
<p>Your audiobooks will be saved in the <code>output_audiobooks</code> directory.</p>

<h3>Command-Line Arguments</h3>
<ul>
    <li><code>--input</code>: Path to the directory containing PDF files.</li>
    <li><code>--output</code>: Path to the directory where audiobooks will be saved.</li>
    <li><code>--voice</code>: Choose the voice type (<code>male</code> or <code>female</code>).</li>
    <li><code>--language</code>: Specify the language for conversion (e.g., <code>en</code> for English).</li>
    <li><code>--rate</code>: Adjust the speech rate (default is <code>1.0</code>).</li>
</ul>

<h2>🧪 Testing</h2>
<p>To run the tests, use:</p>
<pre><code>python -m unittest discover tests</code></pre>



<h2>🤝 Contributing</h2>
<p>Contributions are welcome! Please follow these steps:</p>
<ol>
    <li>Fork the project.</li>
    <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>).</li>
    <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>).</li>
    <li>Open a Pull Request.</li>
</ol>

<h2>🧑‍💻 Author</h2>
<p><strong>Abu Saif Kabbow</strong> - <a href="https://github.com/saifkabbo">saifkabbo</a></p>

<h2>🙏 Acknowledgments</h2>
<p>Thanks to the open-source community for making this project possible.</p>

</body>
</html>
