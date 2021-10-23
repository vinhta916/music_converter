import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { Button, StyleSheet, Text, TextInput, View } from 'react-native';

export default function App() {

  const [url ,setURL] = useState('')

  function saveURL(){
    console.log(url)
  }

  return (
    <View style={styles.container}>
        <Button onPress={saveURL} title='Save' />
        <TextInput type="text" name="url" placeholder="Youtube URL" value={url} onChangeText={setURL} />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
