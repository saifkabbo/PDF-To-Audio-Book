<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF to Audiobook Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #444;
        }
        h2 {
            color: #555;
            border-bottom: 2px solid #ddd;
            padding-bottom: 5px;
        }
        p {
            line-height: 1.6;
        }
        code {
            background-color: #f4f4f4;
            border-radius: 4px;
            padding: 2px 4px;
        }
        pre {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            margin: 0;
            padding: 0;
            list-style: none;
        }
        ul li {
            background: #eee;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .code-block {
            background-color: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            overflow-x: auto;
        }
        .code-block code {
            color: #f8f8f2;
            background: none;
            padding: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PDF to Audiobook Converter</h1>

        <h2>🚀 Overview</h2>
        <p>
            The <strong>PDF to Audiobook Converter</strong> is a powerful tool that transforms your PDF documents into audiobooks. This tool leverages text-to-speech (TTS) technology, allowing you to listen to your favorite books, articles, or any other PDFs while on the go. Perfect for those who prefer audio content or need to multitask.
        </p>

        <h2>🎯 Features</h2>
        <ul>
            <li><strong>PDF to Audio Conversion</strong>: Effortlessly convert any PDF into an audiobook.</li>
            <li><strong>Multi-Language Support</strong>: Supports conversion in multiple languages.</li>
            <li><strong>Customizable Voices</strong>: Choose from different voice options and adjust speech rates to suit your preferences.</li>
            <li><strong>Batch Processing</strong>: Convert multiple PDF files in one go.</li>
            <li><strong>Output Formats</strong>: Save the audiobook in popular audio formats like MP3.</li>
        </ul>

        <h2>🛠️ Installation</h2>
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.x</li>
            <li>Pip (Python package manager)</li>
        </ul>

        <h3>Install Dependencies</h3>
        <p>First, clone the repository:</p>
        <div class="code-block"><pre><code>git clone https://github.com/your-username/pdf-to-audiobook-converter.git
cd pdf-to-audiobook-converter</code></pre></div>

        <p>Then, install the required Python packages:</p>
        <div class="code-block"><pre><code>pip install -r requirements.txt</code></pre></div>

        <h2>🚀 Usage</h2>
        <ol>
            <li>Place your PDF files in the <code>input_pdfs</code> directory.</li>
            <li>Run the conversion script:</li>
        </ol>
        <div class="code-block"><pre><code>python convert_to_audio.py --input input_pdfs --output output_audiobooks --voice male --language en --rate 1.0</code></pre></div>
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
        <div class="code-block"><pre><code>python -m unittest discover tests</code></pre></div>

        <h2>📄 License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

        <h2>🤝 Contributing</h2>
        <p>Contributions are welcome! Please read the <a href="CONTRIBUTING.md">CONTRIBUTING</a> guidelines first.</p>
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
    </div>
</body>
</html>
