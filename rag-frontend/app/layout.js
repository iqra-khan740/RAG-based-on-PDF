import './globals.css';

export const metadata = {
  title: 'RAG Chat App',
  description: 'Chat with your PDF documents',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
