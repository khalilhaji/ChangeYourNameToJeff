<template>
  <div class="input">
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-layout row wrap>
      <v-flex xs12 sm6 md4>
    <v-text-field
      v-model="current_name_first"
      :rules="rules"
      label="Current First Name"
      required
    ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md4>
  <v-text-field
  v-model="current_name_middle"
  label="Current Middle Name"
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md4>
  <v-text-field
  v-model="current_name_last"
  :rules="rules"
  label="Current Last Name"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md9>
  <v-text-field
  v-model="current_address_street"
  :rules="rules"
  label="Address"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md1>
  <v-text-field
  v-model="current_address_apt"
  :rules="rules"
  label="Apt."
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md1>
  <v-select
  v-model="current_address_state"
  :rules="rules"
  label="State"
  :items="states"
  required
  ></v-select>
  </v-flex>
  <v-flex xs12 sm6 md1>
  <v-text-field
  v-model="current_address_zip"
  :counter="5"
  :rules="rules"
  label="ZIP Code"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md5>
  <v-select
  v-model="county"
  :rules="rules"
  :items="counties"
  label="County"
  required
  ></v-select>
  </v-flex>


  <v-flex xs12 sm6 md2>
    <v-checkbox
    v-model="mail_same"
    label="Mailing address different?"
    ></v-checkbox>
  </v-flex>
  <v-flex xs12 sm6 md9>
    <v-text-field
    v-model="mailing_address_street"
    v-if="mail_same"
    label="Mailing Address"
    ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md1>
  <v-text-field
  v-model="mailing_address_apt"
  v-if="mail_same"
  label="Apt."
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md1>
  <v-select
  v-model="mailing_address_state"
  label="State"
  v-if="mail_same"
  :items="states"
  ></v-select>
  </v-flex>
  <v-flex xs12 sm6 md1>
  <v-text-field
  v-model="mailing_address_zip"
  :counter="5"
  v-if="mail_same"
  label="ZIP Code"
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md6>
  <v-text-field
  v-model="primary_phone"
  :rules="rules"
  label="Primary Phone"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md6>
  <v-text-field
  v-model="email_address"
  :rules="rules"
  label="E-Mail"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md2>
  <v-checkbox
  v-model="prior_name_no"
  label="Do You Have a Prior Name?"
  ></v-checkbox>
  </v-flex>
  <v-flex xs12 sm6 md10>
    <v-text-field
    v-model="prior_name_from"
    v-if="prior_name_no"
    label="Prior Name"
    ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md3>
  <v-checkbox
  v-model="return_documents_yes"
  label="Return Documents?"
  ></v-checkbox>
  </v-flex>
  <v-flex xs12 sm6 md3>
  <v-text-field
  disabled
  value="Jeff"
  :rules="rules"
  label="New Name"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md6>
  <v-text-field
  v-model="reason"
  :rules="rules"
  label="Reason"
  required
  ></v-text-field>
  </v-flex>
  <v-flex xs12 sm6 md4>
   <v-dialog
     ref="dialog"
     v-model="modal"
     :return-value.sync="date"
     persistent
     lazy
     full-width
     width="290px">
     <v-text-field
       slot="activator"
       v-model="date"
       label="Date of Birth"
       prepend-icon="event"
       readonly
     ></v-text-field>
     <v-date-picker v-model="date" scrollable>
       <v-spacer></v-spacer>
       <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
       <v-btn flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
     </v-date-picker>
   </v-dialog>
   </v-flex>
   <v-flex xs12 sm6 md4>
   <v-text-field
   v-model="mothers_maiden_name"
   :rules="rules"
   label="Mother's Maiden Name"
   required
   ></v-text-field>
   </v-flex>
   <v-flex xs12 sm6 md4>
   <v-text-field
   v-model="ssn_last_four"
   :rules="rules"
   label="Last 4 of SSN"
   required
   ></v-text-field>
   </v-flex>
<v-flex xs12 sm12 md12>
    <v-btn
      :disabled="!valid"
      @click="submit"
    >
      submit
    </v-btn>
    <v-btn @click="clear">clear</v-btn>
  </v-flex>
  </v-layout>
  </v-form>
</div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Input',
    data: () => ({
      mail_same: false,
      prior_name_no: false,
      current_name_first: '',
      current_name_middle: '',
      current_name_last: '',
      county: '',
      current_address_street: '',
      current_address_apt: '',
      current_address_state: '',
      current_address_zip: '',
      primary_phone: '',
      email_address: '',
      return_documents_yes: true,
      mothers_maiden_name: '',
      ssn_last_four: '',
      date: '',
      reason: "I don't want to have my current name anymore. It should be Jeff.",
      modal: false,
      valid: true,
      name: '',
      rules: [
        v => !!v || 'This field is required',
      ],
      email: '',
      counties: [
        'Barnstable',
        'Berkshire',
        'Bristol',
        'Dukes',
        'Essex',
        'Franklin',
        'Hampden',
        'Hampshire',
        'Middlesex',
        'Nantucket',
        'Norfolk',
        'Plymouth',
        'Suffolk',
        'Worcester'
      ],
      states: ['MA'],
      mailing_address_street: '',
      mailing_address_apt: '',
      mailing_address_zip: '',
      mailing_address_state: ''
    }),
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
          // Native form submission is not yet supported


          axios.post('https://us-central1-changemynametojeff.cloudfunctions.net/function-1', {
            template: 'massachusetts.pdf',
            form_values: {
              current_name_first: this.current_name_first,
              current_name_middle: this.current_name_middle,
              current_name_last: this.current_name_last,
              county: this.county,
              current_address_street: this.current_address_street,
              current_address_apt: this.current_address_apt,
              current_address_state: this.current_address_state,
              current_address_zip: this.current_address_zip,
              primary_phone: this.primary_phone,
              email_address: this.email_address,
              prior_name_no: this.prior_name_no ? "X" : "",
              return_documents_yes: this.return_documents_yes,
              first_name_jeff: "Jeff",
              reason: this.reason,
              current_name_full: this.current_name_first + " " + this.current_name_middle + " " + this.current_name_last,
              mothers_maiden_name: this.mothers_maiden_name,
              ssn_last_four: this.ssn_last_four,
              prior_name_from: this.prior_name_from,
              prior_name_to: this.current_name_full,
              prior_name_reason: this.reason,
              prior_name_yes: this.prior_name_no ? "X" : "",
              middle_name_jeff: "",
              last_name_jeff: "",
              mailing_address_street: this.mailing_address_street,
              mailing_address_apt: this.mailing_address_apt,
              mailing_address_city: "",
              mailing_address_state: this.mailing_address_state,
              mailing_address_zip: this.mailing_address_zip,
              dob: this.date
          }
        }).then(function(res) {
          console.log(res);
        })
        }
      },
      clear () {
        this.$refs.form.reset()
      }
    }
  }
</script>
<style scoped>
  .input {
    margin: 150px;
  }
</style>
