'use client';
import { useState } from 'react';

export default function FileUploader() {
  const [file, setFile] = useState(null);

  const uploadFile = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('/api/upload/route', {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    alert(data.message);
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadFile}>Upload PDF</button>
    </div>
  );
}
