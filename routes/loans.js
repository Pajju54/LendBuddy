import express from 'express';
import { check, validationResult } from 'express-validator';
import auth from '../middleware/auth.js';
import Loan from '../models/Loan.js';
import User from '../models/User.js';

const router = express.Router();

// @route   POST api/loans
// @desc    Create a new loan application
// @access  Private
router.post('/', [
    auth,
    check('fullName', 'Full name is required').not().isEmpty(),
    check('email', 'Email is required').isEmail(),
    check('phone', 'Phone number is required').not().isEmpty(),
    check('loanType', 'Loan type is required').isIn(['personal', 'home', 'car', 'education', 'business']),
    check('loanAmount', 'Loan amount is required').isNumeric(),
    check('loanTenure', 'Loan tenure is required').isNumeric(),
    check('maxInterestRate', 'Maximum interest rate is required').isNumeric(),
    check('monthlyIncome', 'Monthly income is required').isNumeric(),
    check('employmentType', 'Employment type is required').not().isEmpty(),
    check('purpose', 'Loan purpose is required').not().isEmpty()
], async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    try {
        const {
            fullName,
            email,
            phone,
            loanType,
            loanAmount,
            loanTenure,
            maxInterestRate,
            monthlyIncome,
            employmentType,
            purpose
        } = req.body;

        // Create new loan
        const newLoan = new Loan({
            borrower: req.user.id,
            fullName,
            email,
            phone,
            loanType,
            loanAmount,
            loanTenure,
            maxInterestRate,
            monthlyIncome,
            employmentType,
            purpose
        });

        const loan = await newLoan.save();
        res.json(loan);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

// @route   GET api/loans
// @desc    Get all loan applications (for bank dashboard)
// @access  Public (would be restricted in production)
router.get('/', async (req, res) => {
    try {
        const loans = await Loan.find().sort({ createdAt: -1 });
        res.json(loans);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

// @route   GET api/loans/user
// @desc    Get all loans for current user
// @access  Private
router.get('/user', auth, async (req, res) => {
    try {
        const loans = await Loan.find({ borrower: req.user.id }).sort({ createdAt: -1 });
        res.json(loans);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server Error');
    }
});

// @route   POST api/loans/:id/offer
// @desc    Make an offer on a loan (for banks)
// @access  Private
router.post('/:id/offer', [
    auth,
    check('interestRate', 'Interest rate is required').isNumeric()
], async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    try {
        const loan = await Loan.findById(req.params.id);

        if (!loan) {
            return res.status(404).json({ msg: 'Loan not found' });
        }

        // Add new offer
        loan.offers.unshift({
            bank: req.user.id,
            interestRate: req.body.interestRate
        });

        await loan.save();
        res.json(loan);
    } catch (err) {
        console.error(err.message);
        if (err.kind === 'ObjectId') {
            return res.status(404).json({ msg: 'Loan not found' });
        }
        res.status(500).send('Server Error');
    }
});

export default router;