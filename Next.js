'use client';

import React, { useState } from 'react';
import { createBaseAccountSDK, pay, getPaymentStatus } from '@base-org/account';
import { SignInWithBaseButton, BasePayButton } from '@base-org/account-ui/react';

export default function Home() {
  const [isSignedIn, setIsSignedIn] = useState(false);
  const [paymentStatus, setPaymentStatus] = useState('');
  const [paymentId, setPaymentId] = useState('');

  // آپ کے بزنس کی شناخت کے ساتھ SDK کی ترتیب
  const sdk = createBaseAccountSDK({
    appName: 'Marwa Property Advisors',
    appLogoUrl: 'https://base.org/logo.png', // یہاں آپ اپنے لوگو کا لنک لگا سکتے ہیں
  });

  const handleSignIn = async () => {
    try {
      await sdk.getProvider().request({ method: 'wallet_connect' });
      setIsSignedIn(true);
    } catch (error) {
      console.error('سائن ان میں دشواری:', error);
    }
  };

  const handlePayment = async () => {
    try {
      const { id } = await pay({
        amount: '1.00', // یہاں اپنی مرضی کی رقم (USD میں) لکھیں
        to: 'jamilahmed.base.eth', // آپ کا رجسٹرڈ بیس ایڈریس
        testnet: false // اصلی ادائیگی کے لیے
      });

      setPaymentId(id);
      setPaymentStatus('ادائیگی کا عمل شروع ہو گیا ہے۔');
    } catch (error) {
      console.error('ادائیگی میں خرابی:', error);
      setPaymentStatus('ادائیگی مکمل نہیں ہو سکی۔');
    }
  };

  const handleCheckStatus = async () => {
    if (!paymentId) return;
    try {
      const { status } = await getPaymentStatus({ id: paymentId });
      setPaymentStatus(`ادائیگی کی تازہ ترین صورتحال: ${status}`);
    } catch (error) {
      setPaymentStatus('اسٹیٹس معلوم کرنے میں خرابی۔');
    }
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#000', color: '#fff', display: 'flex', justifyContent: 'center', alignItems: 'center', fontFamily: 'Arial' }}>
      <div style={{ backgroundColor: '#111', padding: '40px', borderRadius: '20px', textAlign: 'center', border: '1px solid #333', width: '350px' }}>
        <h2 style={{ color: '#0052ff', marginBottom: '5px' }}>Marwa Property</h2>
        <p style={{ fontSize: '12px', color: '#666', marginBottom: '30px' }}>Secure Digital Payments</p>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          <SignInWithBaseButton variant="solid" colorScheme="dark" onClick={handleSignIn} />
          
          <BasePayButton colorScheme="dark" onClick={handlePayment} />
          
          {paymentId && (
            <button 
              onClick={handleCheckStatus} 
              style={{ background: '#222', color: '#fff', border: '1px solid #444', padding: '10px', borderRadius: '8px', cursor: 'pointer' }}>
              اسٹیٹس چیک کریں
            </button>
          )}
        </div>

        {paymentStatus && (
          <div style={{ marginTop: '20px', fontSize: '14px', color: '#00ff00', padding: '10px', backgroundColor: '#002200', borderRadius: '5px' }}>
            {paymentStatus}
          </div>
        )}
      </div>
    </div>
  );
}
