import Header from '../app/components/Header';
import Footer from '../app/components/Footer';
import AudioForm from '../app/components/AudioForm';

export default function Home() {
  return (
    <div className = 'home-div'>
      <Header></Header>
        <main className = "home-content">
          <AudioForm></AudioForm>
        </main>
      <Footer></Footer>
    </div>
    
  );
}
