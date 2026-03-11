import React from 'react';
import Demo from './Demo';
import Header from './component/Header';
import Hero from './component/Hero';
import ContactForm from './component/ContactForm';
import Footer from './component/Footer';

const App = () => {
  return (
    <div>
      <Header/>
      <Hero/>
      <ContactForm/>
      <Footer/>
    </div>
  );
};

export default App;