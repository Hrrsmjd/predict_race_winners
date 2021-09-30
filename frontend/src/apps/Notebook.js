import { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';
import '../App.css';
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function Notebook() {
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  return (
    <div className="Notebook">
      <Document 
        file="test.pdf"
        onLoadSuccess={onDocumentLoadSuccess}
      >
        <Page pageNumber={pageNumber}/>
      </Document>
      <p>Page {pageNumber} of {numPages}</p>
    </div>
  );
}

export default Notebook;
