- name: Run Workflow
  id: write_file
  uses: timheuer/base64-to-file@v1.1
  with:--
    fileName: 'myTemporaryFile.txt'
    encodedString: ${{ secrets.SOME_ENCODED_STRING }}
