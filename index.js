'use strict'

const { /*exec,*/ execSync } = require('child_process')
//const net = require('net')
//const delay = require('delay')

const nfc = async () => {
  console.log((await execSync(`python3 testNfc.py`)).toString().replace(/\n/,''))
  nfc()
}
nfc()

/*

const pythonProcessId = exec(`python3 test.py`, () => {})

const processExit = async () => {
  process.kill(pythonProcessId.pid + 1)
  await delay(500)
  process.exit(0)
}

const server = net.createServer((connection) => {
  connection.on('close', () => {})
  connection.on('data', (data) => {
    console.log(data)
  })
  connection.on('error', (err) => {
    console.error(err.message)
  })
  connection.write('unix domain socket')
  connection.end()
})

try {
  fs.unlinkSync('/tmp/nfcTest.sock')
} catch (error) {}

server.listen('/tmp/nfcTest.sock')
*/
